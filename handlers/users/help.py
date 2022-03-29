from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Команди для використання бота:\n ",
            "/start - Розпочинає роботу з ботом\n",
            "/help - Отримати список команд\n",
            "/start_poll - Розпочинає опитування\n",
            "/correct_answers - Розпочинає опитування та дозволяє виправити помилки\n",
            "/generate_result - Видає результати розрахунків\n")

    await message.answer("\n".join(text))
