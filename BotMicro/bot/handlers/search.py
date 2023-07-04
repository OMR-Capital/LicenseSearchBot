from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import messages
from search_utils.search import get_items_by_query


router = Router()


@router.message(F.text)
async def query_handler(message: Message, state: FSMContext):
    if not message.text:
        return

    await message.answer(messages.WAIT_SEARCH)

    items = await get_items_by_query(message.text, limit=30)
    
    if items:
        for i in range(0, len(items), 10):
            items_slice = items[i:i + 10]
            await message.answer(messages.get_items_form(items_slice))
    else:
        await message.answer(messages.ITEMS_NOT_FOUND)

    await message.answer(messages.SEARCH_FINISHED)
    await state.clear()
