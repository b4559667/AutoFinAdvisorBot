from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsWholeNumber(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        try:
            if int(message.text) == float(message.text):
                return True
        except:
            await message.answer("Введіть ціле число!")
            return False
