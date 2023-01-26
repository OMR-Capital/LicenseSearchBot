from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot import messages


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(messages.GREETING)