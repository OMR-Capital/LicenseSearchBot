from typing import Optional
from aiogram.filters.callback_data import CallbackData


class StartSearchCallback(CallbackData, prefix='search'):
    previous_package_key: Optional[str]