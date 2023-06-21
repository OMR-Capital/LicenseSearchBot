from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot import messages
from bot.keyboards.search import start_search_kb


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        messages.GREETING,
        reply_markup=start_search_kb(None)
    )
