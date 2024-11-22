import asyncio
import logging


from aiogram import Dispatcher

from vakyt_bot.config import bot
from vakyt_bot.handlers.general import general_router

# Bot
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
dp.include_routers(general_router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
