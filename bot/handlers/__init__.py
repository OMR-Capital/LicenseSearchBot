from aiogram import Router

from . import start, search


router = Router()
router.include_router(start.router)
router.include_router(search.router)