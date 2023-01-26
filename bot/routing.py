from aiogram import Dispatcher

from bot.handlers import router


def register_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(router)