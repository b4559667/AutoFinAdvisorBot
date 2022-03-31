from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .number_filter import IsNumber
from .y_greater import IsYGreaterZ
from .t1_greater import IsTGreaterZ
from .deviation_filter import IsDevInBound

if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    pass
