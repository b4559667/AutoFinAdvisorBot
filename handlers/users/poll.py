from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test
from utils.misc import Calculations


# Начало опроса
@dp.message_handler(Command("start_poll"), state=None)
async def start_poll(message: types.Message):
    await message.answer("Enter your average annual income:")
    await Test.q1_income_state.set()


@dp.message_handler(state=Test.q1_income_state)
async def answer_start_age(message: types.Message, state: FSMContext):
    avg_income_data = message.text
    await state.update_data(avg_income_data=avg_income_data)
    await message.answer("What age do you plan to start saving:")
    await Test.q2_start_invest_state.set()


@dp.message_handler(state=Test.q2_start_invest_state)
async def answer_end_age(message: types.Message, state: FSMContext):
    start_invest_data = message.text
    await state.update_data(start_invest_data=start_invest_data)
    await message.answer("What age do you plan to stop saving:")
    await Test.q3_end_invest_state.set()


@dp.message_handler(state=Test.q3_end_invest_state)
async def answer_use_age(message: types.Message, state: FSMContext):
    end_invest_data = message.text
    await state.update_data(end_invest_data=end_invest_data)
    await message.answer("Until what age do you plan to use savings:")
    await Test.q4_use_invest_state.set()


@dp.message_handler(state=Test.q4_use_invest_state)
async def answer_interest(message: types.Message, state: FSMContext):
    use_invest_data = message.text
    await state.update_data(use_invest_data=use_invest_data)
    await message.answer("Enter nominal annual interest rate:")
    await Test.q5_rate_state.set()


@dp.message_handler(state=Test.q5_rate_state)
async def answer_deviation(message: types.Message, state: FSMContext):
    rate_data = message.text
    await state.update_data(rate_data=rate_data)
    await message.answer("Enter critical decrease of the interest rate:")
    await Test.q6_rate_dv_state.set()


@dp.message_handler(state=Test.q6_rate_dv_state)
async def display_info(message: types.Message, state: FSMContext):  # answer deviation
    rate_dv_data = message.text
    await state.update_data(rate_dv_data=rate_dv_data)
    data = await state.get_data()
    await message.answer("Your data: \n\n"
                         "Average annual income - {avg_income_data}\n"
                         "Staring age - {start_invest_data}\n"
                         "Completion age - {end_invest_data}\n"
                         "Using age - {use_invest_data}\n"
                         "Interest rate - {rate_data}\n"
                         "Deviation - {rate_dv_data}\n"
                         "Is that correct? You can answer questions again using /correct_data\n".format(
        avg_income_data=data.get("avg_income_data"), start_invest_data=data.get("start_invest_data"),
        end_invest_data=data.get("end_invest_data"), use_invest_data=data.get("use_invest_data"),
        rate_data=data.get("rate_data"), rate_dv_data=data.get("rate_dv_data")))

    await Test.generate_result_state.set()


@dp.message_handler(Command("correct_answers"), state=Test.generate_result_state)
async def restart_poll(message: types.Message, state: FSMContext):
    await state.finish()
    await start_poll(message)


@dp.message_handler(Command("generate_result"), state=Test.generate_result_state)
async def generate_result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    result = Calculations(int(data['avg_income_data']), int(data['start_invest_data']),
                          int(data['end_invest_data']),
                          int(data['use_invest_data']), int(data['rate_data']), int(data['rate_dv_data']))
    await message.answer("pee pee poo poo SOMETHING CALCULATING {}".format(str(result.calc_result())))
    await state.finish()
