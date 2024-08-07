# from aiogram import executor as ex
# from commands import start
import logging
import sys

from aiogram import Bot
from globals import dp, Config
from aiogram.client.session.middlewares.request_logging import RequestLogging
from aiogram.methods import GetUpdates
import asyncio

# async def bot_callback(x):
#     print("Started")

async def main()->None:
    bot = Bot(token=Config.TG_TOKEN)
    bot.session.middleware(RequestLogging(ignore_methods=[GetUpdates]))
    await dp.start_polling(bot, allowed_updates=["message"])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
