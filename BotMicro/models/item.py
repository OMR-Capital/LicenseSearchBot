from typing import Any
from odetam.async_model import AsyncDetaModel


class Item(AsyncDetaModel):
    name: str
    code: str
    hazard: str
    allowed_works: list[str]
    address: str
    company: str

    class Config:
        table_name = 'items'
