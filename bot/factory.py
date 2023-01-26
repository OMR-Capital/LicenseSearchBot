from aiogram import Bot, Dispatcher
from aiogram_deta.storage import DetaStorage
from deta import Deta

from bot.routing import register_routers


def create_bot(token: str) -> Bot:
    bot = Bot(token, parse_mode='HTML')
    return bot


def crete_dispatcher(deta: Deta) -> Dispatcher:
    base = deta.AsyncBase('fsm')
    storage = DetaStorage(base)
    dispatcher = Dispatcher(storage=storage)
    register_routers(dispatcher)
    return dispatcher
