"""Pagination helpers for list endpoints."""


def paginate(items, page, page_size):
    """Return the items on a 1-indexed page."""
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be >= 1")
    start = (page - 1) * page_size
    return items[start:start + page_size]


def page_count(total, page_size):
    """Return how many pages are needed to show `total` items."""
    if page_size < 1:
        raise ValueError("page_size must be >= 1")
    return total // page_size
