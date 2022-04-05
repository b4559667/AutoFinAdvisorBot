from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users.help import bot_help
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}!")
    await bot_help(message)
