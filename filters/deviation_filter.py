from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsDevInBound(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        content = float(message.text)
        #g await message.answer(message.text)
        if 0 < content <= 100:
            return True
        else:
            await message.answer('Число має бути більше 0 та менше або дорівнювати 100')
            return False
