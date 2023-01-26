from search_utils.fuzzy_search import fuzzy_search
from search_utils.direct_search import direct_search

from models import Item


async def get_items_by_code(code: str) -> list[Item]:
    items: list[Item] = await Item.query(Item.code == code)
    return items


async def get_items_by_name(name: str) -> list[Item]:
    items: list[Item] = await Item.get_all()
    direct_search_result = set(direct_search(name, items))
    fuzzy_search_result = set(fuzzy_search(name, items))
    relevant_items = direct_search_result | fuzzy_search_result
    return list(relevant_items)
