#!/usr/bin/env python3
"""gv g"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Tgv
    Args:
        page (int): p
        page_size (int): v
    Return:
        t
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """Sgv f"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """fgg g"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                rr = csv.reader(f)
                dataset = [f for f in rr]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Tecv
        Args:
            page (int): r
            page_size (int): n
        Return:
            l
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        dl = len(dataset)
        try:
            i = index_range(page, page_size)
            return dataset[i[0]:i[1]]
        except IndexError:
            return []
