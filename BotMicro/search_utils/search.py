from typing import Optional
from search_utils.fuzzy_search import fuzzy_search
from search_utils.direct_search import direct_search

from models import Item


async def get_items_by_query(
    query: str,
    limit: Optional[int] = None,
) -> list[Item]:
    prepared_query = query.replace(' ', '').strip()
    if prepared_query.isdigit() and len(prepared_query) > 9:
        return await get_items_by_code(prepared_query, limit)
    else:
        return await get_items_by_name(query, limit)


async def get_items_by_code(
    code: str,
    limit: Optional[int] = None,
) -> list[Item]:
    items: list[Item] = await Item.query(Item.code == code)
    return items[:limit] if limit else items


async def get_items_by_name(
    name: str,
    limit: Optional[int] = None,
) -> list[Item]:
    items: list[Item] = await Item.get_all()
    direct_search_result = direct_search(name, items, limit)
    fuzzy_search_result = fuzzy_search(name, items, limit)

    relevant_items = direct_search_result.copy()
    for item in fuzzy_search_result:
        if item not in direct_search_result:
            relevant_items.append(item)

    return relevant_items[:limit] if limit else relevant_items
