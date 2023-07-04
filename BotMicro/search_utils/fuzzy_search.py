from typing import Optional
from fuzzywuzzy import fuzz

from models import Item
from search_utils.utils import normalize


def fuzzy_search(query: str, items: list[Item], limit: Optional[int] = None) -> list[Item]:
    query = normalize(query)
    query_words = query.split()
    min_score = len(query_words) * 85

    scored_items: list[tuple[Item, int]] = []
    for item in items:
        score = 0
        item_name = normalize(item.name)
        for word in query_words:
            score += fuzz.partial_ratio(word, item_name)  # type: ignore

        if score >= min_score:
            scored_items.append((item, score))

        if limit and len(scored_items) >= limit:
            break

    scored_items.sort(key=lambda pair: pair[1], reverse=True)
    relevant_items = [item for item, score in scored_items]
    return relevant_items
