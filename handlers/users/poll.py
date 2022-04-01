from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsNumber, IsYGreaterZ, IsTGreaterZ, IsDevInBound
from loader import dp
from aiogram import types

from states import PollStates
from utils.misc import Calculations


# Начало опроса
@dp.message_handler(Command("cancel_poll"),
                    state=[PollStates.q1_income_state, PollStates.q2_start_invest_state, PollStates.q3_end_invest_state,
                           PollStates.q4_use_invest_state, PollStates.q5_rate_state, PollStates.q6_rate_dv_state,
                           PollStates.generate_result_state])
async def cancel_poll(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ви зупинили опитування")


@dp.message_handler(Command("start_poll"), state=None)
async def start_poll(message: types.Message):
    await message.answer("Який ви маєте середній щорічний прибуток? <em>Наприклад: 100000 грн</em>")
    await PollStates.q1_income_state.set()


@dp.message_handler(IsNumber(), IsYGreaterZ(), state=PollStates.q1_income_state)
async def answer_start_age(message: types.Message, state: FSMContext):
    avg_income_data = message.text
    await state.update_data(avg_income_data=avg_income_data)
    await message.answer(
        "З якого віку ви плануєте запровадити власну програму заощадження? <em>Наприклад: 35 років</em>")
    await PollStates.q2_start_invest_state.set()


@dp.message_handler(IsNumber(), IsTGreaterZ(), state=PollStates.q2_start_invest_state)
async def answer_end_age(message: types.Message, state: FSMContext):
    start_invest_data = message.text
    await state.update_data(start_invest_data=start_invest_data)
    await message.answer("В якому віці ви плануєте завершити власну програму заощадження? <em>Наприклад: 60 років</em>")
    await PollStates.q3_end_invest_state.set()


@dp.message_handler(IsNumber(), state=PollStates.q3_end_invest_state)
async def answer_use_age(message: types.Message, state: FSMContext):
    end_invest_data = message.text
    data = await state.get_data()
    if float(data['start_invest_data']) < float(end_invest_data):
        await state.update_data(end_invest_data=end_invest_data)
        await message.answer(
            "До якого віку ви плануєте використовувати власний фонд заощадження? <em>Наприклад: 80 років</em>")
        await PollStates.q4_use_invest_state.set()
    else:
        await message.answer("Вік завершення програми заощаджень має бути більшим за вік запровадження!")  # notify user

        # await answer_end_age(message, state) multiple variants
        @dp.message_handler(IsNumber(), IsTGreaterZ(), state=PollStates.q2_start_invest_state)
        async def answer_end_age(message: types.Message, state: FSMContext):
            start_invest_data = message.text
            await state.update_data(start_invest_data=start_invest_data)
            await message.answer(
                "В якому віці ви плануєте завершити власну програму заощадження? <em>Наприклад: 60 років</em>")
            await PollStates.q3_end_invest_state.set()


@dp.message_handler(IsNumber(), state=PollStates.q4_use_invest_state)
async def answer_interest(message: types.Message, state: FSMContext):
    use_invest_data = message.text
    data = await state.get_data()
    if float(data['end_invest_data']) < float(use_invest_data):
        await state.update_data(use_invest_data=use_invest_data)
        await message.answer(
            "Яку номінальну річну відсоткову ставку на заощадження Ви очікуєте отримувати? <em>Наприклад: 10 %</em>")
        await PollStates.q5_rate_state.set()
    else:
        await message.answer("Вік використання програми заощаджень має бути більшим за вік завершення!")

        @dp.message_handler(IsNumber(), state=PollStates.q3_end_invest_state)
        async def answer_use_age(message: types.Message, state: FSMContext):
            end_invest_data = message.text
            data = await state.get_data()
            if float(data['start_invest_data']) < float(end_invest_data):
                await state.update_data(end_invest_data=end_invest_data)
                await message.answer(
                    "До якого віку Ви плануєте використати власний фонд заощадження? <em>Наприклад: 80 років</em>")
                await PollStates.q4_use_invest_state.set()


@dp.message_handler(IsNumber(), IsYGreaterZ(), state=PollStates.q5_rate_state)
async def answer_deviation(message: types.Message, state: FSMContext):
    rate_data = message.text
    await state.update_data(rate_data=rate_data)
    await message.answer(
        "Яке зменшення у відсотках від визначеної вами середньої дохідності"
        " буде для вас критичним у прийнятті рішення переглянути (припинити) програму заощаджень? <em>Наприклад: 30%</em>")
    await PollStates.q6_rate_dv_state.set()


@dp.message_handler(IsNumber(), IsDevInBound(), state=PollStates.q6_rate_dv_state)
async def display_info(message: types.Message, state: FSMContext):  # answer deviation
    rate_dv_data = message.text
    await state.update_data(rate_dv_data=rate_dv_data)
    data = await state.get_data()
    await message.answer("Введена інформація: \n\n"
                         "Cередній щорічний прибуток - {avg_income_data} грн\n"
                         "Вік запровадження програми заощаджень - {start_invest_data} років\n"
                         "Вік завершення програми заощаджень - {end_invest_data} років\n"
                         "Вік використання заощаджень - {use_invest_data} років\n"
                         "Номінальна річна відсоткова ставка - {rate_data}%\n"
                         "Відсоткове відхилення від номінальної річної ставки - {rate_dv_data}%\n"
                         "\nЧи коректно заповнена інформація? <em>\nВи можете знову пройти опитування "
                         "для виправлення помилок використовуючи команду</em> - /correct_answers\n"
                         "\nДля отримання результату: \n<em>Використовуйте команду</em> - /generate_result".format(
        avg_income_data=data.get("avg_income_data"), start_invest_data=data.get("start_invest_data"),
        end_invest_data=data.get("end_invest_data"), use_invest_data=data.get("use_invest_data"),
        rate_data=data.get("rate_data"), rate_dv_data=data.get("rate_dv_data")))

    await PollStates.generate_result_state.set()


@dp.message_handler(Command("correct_answers"), state=PollStates.generate_result_state)
async def restart_poll(message: types.Message, state: FSMContext):
    await state.finish()
    await start_poll(message)


@dp.message_handler(Command("generate_result"), state=PollStates.generate_result_state)
async def generate_result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    calculate = Calculations(data['avg_income_data'], data['start_invest_data'],
                             data['end_invest_data'],
                             data['use_invest_data'], data['rate_data'], data['rate_dv_data'])
    result = calculate.calc_result()
    await message.answer(
        "Для забезпечення постійного рівня споживання від <em>{start_invest_data} до "
        "{use_invest_data}</em> років у розмірі <em>{C} грн.</em> "
        "Вам потрібно щороку заощаджувати <em>{S} грн.</em> на рік під номінальну відсоткову ставку <em>{rate_data}%.</em>".format(
            start_invest_data=data["start_invest_data"],
            use_invest_data=data["use_invest_data"],
            C=result[1], S=result[0],
            rate_data=data['rate_data']))
    await state.finish()
