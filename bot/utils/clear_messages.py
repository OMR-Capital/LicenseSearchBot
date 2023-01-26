from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from odetam.exceptions import ItemNotFound

from models import MessagesPackage


async def clear_messages(messages_package_key: str):
    try:
        messages_package: MessagesPackage = await MessagesPackage.get(messages_package_key) 
    except ItemNotFound:
        return
    
    bot = Bot.get_current()
    if not bot:
        return
    
    for message_id in messages_package.messages_ids:
        try:
            await bot.delete_message(
                messages_package.chat_id,
                message_id
            )
        except TelegramBadRequest:
            continue
    