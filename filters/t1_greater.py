from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsTGreaterZ(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        if float(message.text) > 0:
            return True
        else:
            await message.answer("Ваш вік має бути додатним!")
            return False
