from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Розпочати роботу з ботом"),
            types.BotCommand("help", "Отримати список команд"),
            types.BotCommand("start_poll", "Розпочати опитування"),
            types.BotCommand("correct_answers", "Розпочати опитування для виправлення помилок"),
            types.BotCommand("generate_result", "Отримати результати розрахунків"),
            types.BotCommand("cancel_poll", "Зупинити опитування")
        ]
    )
