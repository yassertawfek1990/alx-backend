#!/usr/bin/env python3
"""Con df"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Ta43
    Args:
        page (int): p
        page_size (int): n
    Return:
        t
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
