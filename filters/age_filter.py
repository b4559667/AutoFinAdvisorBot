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


class IsLess125(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if int(message.text) < 125:
            return True
        else:
            await message.answer("Число має бути меншим за 125")
            return False


class IsLess250(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if int(message.text) < 250:
            return True
        else:
            await message.answer("Число має бути меншим за 250")
            return False
