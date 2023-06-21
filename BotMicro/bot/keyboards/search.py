from typing import Optional

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.callbacks.search import StartSearchCallback


def start_search_kb(previous_package_key: Optional[str]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Начать поиск 🔎',
                callback_data=StartSearchCallback(previous_package_key=previous_package_key).pack()
            )
        ]
    ])
