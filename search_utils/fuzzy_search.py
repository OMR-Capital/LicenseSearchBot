from fuzzywuzzy import fuzz

from models import Item
from search_utils.utils import normalize


def fuzzy_search(query: str, items: list[Item]) -> list[Item]:
    query = normalize(query)    

    search_results: list[tuple[Item, int]] = [
        (item, fuzz.partial_token_sort_ratio(query, item.name))
        for item in items
    ]
    search_results.sort(key=lambda r: r[1], reverse=True)

    relevant_items = [item for item, score in search_results if score > 75]
    return relevant_items
    