from aiogram import types, Dispatcher
from config import bot, dp

import random


@dp.message_handler(lambda message: message.text and message.text.startswith(f"beisbol"))
async def mention_handler(message: types.Message):
    text = message.text.split(maxsplit=1)
    chat_id = message.chat.id
    print(chat_id)
    admins = await bot.get_chat_administrators(chat_id)
    insult = ["ты долбаеб?", "ты даун?", "ты тупой?"]
    admin_list = [f"(@{admin.user.username})" for admin in admins]
    if len(text) > 1 and text[1] == "послать кого-то":
        random_admin = random.choice(admin_list)
        response = f"{random_admin} иди нахуй"
    if len(text) > 1 and text[1] == "кто амсоргуч":
        random_admin = random.choice(admin_list)
        response = f"{random_admin} истинный амсоруч"
    for i in insult:
        if len(text) > 1 and text[1] == i:
            response = f"сам {i.replace('?', '')}"
    if response:
        await message.reply(response)
    else:
        await message.reply("такой команды еще нет")


def register_handlers_base(dp):
    dp.register_message_handler(mention_handler, lambda message: message.text and message.text.startswith("beisbol"))