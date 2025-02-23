import aiogram
from config import bot, dp, Admins
from aiogram import executor
import logging
import commands

async def on_startup(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text='бот активирован!')
        # id = -1002407711468
        # await bot.send_message(chat_id=id, text='динаху')
async def on_shutdown(_):
    for i in Admins:
        await bot.send_message(chat_id=i, text="бот выключен")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, allowed_updates=['callback'], on_startup=on_startup, on_shutdown=on_shutdown)
