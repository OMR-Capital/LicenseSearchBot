from typing import Union
from odetam.async_model import AsyncDetaModel


class Item(AsyncDetaModel):
    name: str
    code: str
    hazard: Union[str, None]
    allowed_works: list[str]
    address: str
    company: str

    class Config:
        table_name = 'items'

    # def __hash__(self) -> int:
    #     return hash(self.key)
