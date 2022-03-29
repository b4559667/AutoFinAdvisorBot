from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояния вопросов
class Test(StatesGroup):
    q1_income_state = State()
    q2_start_invest_state = State()
    q3_end_invest_state = State()
    q4_use_invest_state = State()
    q5_rate_state = State()
    q6_rate_dv_state = State()
    generate_result_state = State()
