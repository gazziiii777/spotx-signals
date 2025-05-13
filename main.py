
import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from logging_config import setup_logger
from core.config import settings
from app.db.database import init_db
from app.bot.handlers import router

logger = setup_logger('main')

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


# async def run_periodically():
#     """Запускает проверку каждые 30 минут."""
#     while True:
#         if await check_condition():  # Если условие True → можно отправить сообщение
#             # Здесь можно вызвать функцию отправки сообщения
#             pass
#         await asyncio.sleep(1800)  # 1800 сек = 30 мину


async def on_startup():
    """Функция, которая выполняется при запуске бота."""
    logging.info("Бот запущен.")
    # bot.send_message(text="hi")



async def on_shutdown():
    """Функция, которая выполняется при остановке бота."""
    logging.info("Бот остановлен.")
    await bot.close()


async def main():
    """Основная функция, которая запускает бота и планировщик."""
    await init_db()
    await on_startup()  # Выполняем startup-логику
    dp.include_router(router)
    await dp.start_polling(bot)  # Запускаем бота в режиме long-polling


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен вручную.")
    finally:
        asyncio.run(on_shutdown())  # Выполняем shutdown-логику
