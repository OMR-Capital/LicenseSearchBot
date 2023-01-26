from typing import Any
from odetam.async_model import AsyncDetaModel


class Item(AsyncDetaModel):
    name: str
    code: str
    hazard: str
    allowed_works: list[str]
    address: str

    class Config:
        table_name = 'items'

    def __hash__(self) -> int:
        return int(self.code)

    def __eq__(self, other: Any) -> bool: 
        if isinstance(other, Item):
            return self.code == other.code
        
        return False