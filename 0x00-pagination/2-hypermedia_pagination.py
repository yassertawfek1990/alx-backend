#!/usr/bin/env python3
"""svfv gr"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Serrfs"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        frvv
        Returns:
            List[List]: T
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                r = csv.reader(f)
                dataset = [f for f in r]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Afgv
        Args:
            value (int): T
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Rcv
        Args:
            page (int): T
            page_size (int): T
        Returns:
            List[List]: T
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            d = dataset[start:end]
        except IndexError:
            d = []
        return d

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Rds
        Args:
            page (int): t
            page_size (int): T
        Returns:
            List[List]: T
        """
        t = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= t else None
        }
        return info
