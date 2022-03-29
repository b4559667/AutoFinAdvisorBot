from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Розпочинає роботу з ботом"),
            types.BotCommand("help", "Отримати список команд"),
            types.BotCommand("start_poll", "Розпочинає опитування"),
            types.BotCommand("correct_answers", "Розпочинає опитування та дозволяє виправити помилки"),
            types.BotCommand("generate_result", "Видає результати розрахунків"),
        ]
    )
