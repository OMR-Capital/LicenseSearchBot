from search_utils.fuzzy_search import fuzzy_search
from search_utils.direct_search import direct_search

from models import Item



async def get_items_by_query(query: str) -> list[Item]:
    prepared_query = query.replace(' ', '').strip()
    if prepared_query.isdigit() and len(prepared_query) > 9:
        return await get_items_by_code(prepared_query)
    else:
        return await get_items_by_name(query)


async def get_items_by_code(code: str) -> list[Item]:
    items: list[Item] = await Item.query(Item.code == code)
    return items


async def get_items_by_name(name: str) -> list[Item]:
    items: list[Item] = await Item.get_all()
    direct_search_result = direct_search(name, items)
    fuzzy_search_result = fuzzy_search(name, items)
    
    relevant_items = direct_search_result.copy()
    for item in fuzzy_search_result:
        if item not in direct_search_result:
            relevant_items.append(item)

    return relevant_items
