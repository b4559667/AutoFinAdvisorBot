from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsDevInBound(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        content = float(message.text)
        await message.answer(message.text)
        if 0 < content <= 100:
            return True
        else:
            await message.answer('перевірка умови h u gran 0 i 100')
            return False
