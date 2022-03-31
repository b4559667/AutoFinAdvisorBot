from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Команди для використання бота:\n ",
            "/help - Дозволяє отримати список команд.\n",
            "/start - Розпочинає роботу з ботом.\n",
            "/start_poll - Розпочинає опитування.\n",
            "/correct_answers - Розпочинає нове опитування для виправлення помилок.\n",
            "/generate_result - Оброблює введену інформацію та проводить розрахунки, по їх завершенню видає користувачу результат.\n\n"
            "/cancel_poll - Дозволяє користувачу зупинити опитування на будь-якому питанні.\n")

    await message.answer("\n".join(text))
