from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot import messages
from bot.callbacks.search import StartSearchCallback
from bot.keyboards.search import start_search_kb
from bot.states.search import SearchState
from bot.utils.clear_messages import clear_messages
from models import Item, MessagesPackage
from search_utils import get_items_by_name, get_items_by_code


router = Router()


@router.callback_query(StartSearchCallback.filter())
async def start_search_handler(query: CallbackQuery, callback_data: StartSearchCallback, state: FSMContext):
    await query.answer()
    
    if callback_data.previous_package_key:
        await clear_messages(callback_data.previous_package_key)

    message = query.message
    if not message:
        return
    
    await message.edit_text(messages.ASK_QUERY)
    await state.set_state(SearchState.query)
    await state.update_data(init_message_id=message.message_id)


@router.message(SearchState.query, F.text)
async def query_handler(message: Message, state: FSMContext):
    if not message.text:
        return

    wait_message = await message.answer(messages.WAIT_SEARCH)

    items: list[Item]
    if message.text.isdigit() and len(message.text) > 9:
        items = await get_items_by_code(message.text)
    else:
        items = await get_items_by_name(message.text)

    search_messages_ids: list[int] = [message.message_id, wait_message.message_id]
    if items:
        items = items[:30]
        for i in range(0, len(items), 10):
            items_slice = items[i:i + 10]
            msg = await message.answer(messages.get_items_form(items_slice))
            search_messages_ids.append(msg.message_id)
    else:
        msg = await message.answer(messages.ITEMS_NOT_FOUND)
        search_messages_ids.append(msg.message_id)

    data = await state.get_data()
    init_message_id = data.get('init_message_id')
    if init_message_id:
        search_messages_ids.append(init_message_id)

    search_messages_package = MessagesPackage(
        chat_id=wait_message.chat.id,
        messages_ids=search_messages_ids
    )
    await search_messages_package.save()

    await wait_message.answer(
        messages.SEARCH_FINISHED,
        reply_markup=start_search_kb(search_messages_package.key)
    )
    await state.clear()
