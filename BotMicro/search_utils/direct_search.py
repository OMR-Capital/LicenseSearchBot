from typing import Optional
from models import Item
from search_utils.utils import normalize


def direct_search(
    query: str,
    items: list[Item],
    limit: Optional[int] = None,
) -> list[Item]:
    query = normalize(query)
    if len(query) > 6:
        query = query[:-1]

    relevant_items = []
    for item in items:
        if query in normalize(item.name):
            relevant_items.append(item)

        if limit and len(relevant_items) >= limit:
            break

    return relevant_items
