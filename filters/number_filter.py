from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsNumber(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        try:
            float(message.text)
            return True
        except Exception:
            await message.answer("Введіть число!")
            return False

