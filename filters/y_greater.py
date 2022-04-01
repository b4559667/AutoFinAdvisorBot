from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsYGreaterZ(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        if float(message.text) > 0:
            return True
        else:
            await message.answer("Число має бути додатним!")
            return False
