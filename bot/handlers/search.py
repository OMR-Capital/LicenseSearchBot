from aiogram import Router, F
from aiogram.types import Message

from bot import messages
from models import Item


router = Router()


@router.message(F.text)
async def search_handler(message: Message):
    if not message.text:
        return
    
    items: list[Item]
    if message.text.isdigit():
        items = await search_by_code(message.text)
    else:
        items = await search_by_name(message.text)

    if items:
        for item in items:
            await message.answer(messages.get_item_form(item))
    else:
        await message.answer(messages.ITEMS_NOT_FOUND)


async def search_by_code(code: str) -> list[Item]:
    items: list[Item] = await Item.query(Item.code == code)    
    return items


async def search_by_name(name: str) -> list[Item]:
    pass