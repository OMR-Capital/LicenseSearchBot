from os import getenv

from aiogram import Router

from utils.env_parse import parse_bool

from .error import router as error_router
from .start import router as start_router
from .search import router as search_router

router = Router()
router.include_router(start_router)
router.include_router(search_router)

if parse_bool(getenv('ENABLE_ERRORS_LOGS', 'false')):
    router.include_router(error_router)
