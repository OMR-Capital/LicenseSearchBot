from aiogram import F, Router
from aiogram.types import Message

from bot import messages
from models import Item
from search_utils import direct_search, fuzzy_search


router = Router()


@router.message(F.text)
async def search_handler(message: Message):
    if not message.text:
        return

    wait_message = await message.answer(messages.WAIT_SEARCH)

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

    await wait_message.delete()


async def search_by_code(code: str) -> list[Item]:
    items: list[Item] = await Item.query(Item.code == code)
    return items


async def search_by_name(name: str) -> list[Item]:
    items: list[Item] = await Item.get_all()
    direct_search_result = set(direct_search(name, items))
    fuzzy_search_result = set(fuzzy_search(name, items))
    relevant_items = direct_search_result | fuzzy_search_result
    return list(relevant_items)
