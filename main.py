from os import getenv

from aiogram_deta.web import create_app
from deta import Deta

from bot.factory import create_bot, crete_dispatcher


TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
assert TELEGRAM_TOKEN

WEBHOOK_SECRET = getenv('WEBHOOK_SECRET')
assert WEBHOOK_SECRET


deta = Deta()

bot = create_bot(TELEGRAM_TOKEN)
dispatcher = crete_dispatcher(deta)

app = create_app(
    deta=deta,
    bot=bot,
    dispatcher=dispatcher,
    webhook_secret=WEBHOOK_SECRET
)
