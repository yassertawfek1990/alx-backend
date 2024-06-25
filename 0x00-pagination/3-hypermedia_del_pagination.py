#!/usr/bin/env python3
"""Tsdc"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Rxc ds"""

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Sxc zdc"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Csacs"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                r = csv.reader(f)
                dataset = [f for f in r]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Rasad"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Resefwb """
        d = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(d.keys())
        pd = []
        dc = 0
        x = None
        start = index if index else 0
        for c, m in d.items():
            if c >= start and dc < page_size:
                pd.append(m)
                dc += 1
                continue
            if dc == page_size:
                x = c
                break
        p = {
            'index': index,
            'next_index': x,
            'page_size': len(pd),
            'data': pd,
        }
        return p
