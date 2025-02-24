from aiogram import types, Dispatcher
from config import bot, dp
import g4f
import random

@dp.message_handler(lambda message: message.text and message.text.startswith("beisbol"))
async def chat_bot(message: types.Message):
    text = message.text.split(maxsplit=1)
    chat_id = message.chat.id
    admins = await bot.get_chat_administrators(chat_id)
    
    response = "Такой команды еще нет"
    insult = ["ты долбаеб?", "ты даун?", "ты тупой?"]
    admin_list = [f"(@{admin.user.username})" for admin in admins if admin.user.username]

    if len(text) > 1:
        command = text[1]

        if command == "послать кого-то" and admin_list:
            random_admin = random.choice(admin_list)
            response = f"{random_admin}, иди нахуй"
        elif command == "кто амсоргуч" and admin_list:
            random_admin = random.choice(admin_list)
            response = f"{random_admin} — истинный амсоргуч"
        elif command in insult:
            response = f"Сам {command.replace('?', '')}"
        else:
            g4f_response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": command}]
                )
            response = g4f_response

    await message.reply(response)
def register_handlers_base(dp):
    dp.register_message_handler(chat_bot, lambda message: message.text and message.text.startswith("beisbol"))
    