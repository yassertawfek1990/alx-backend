#!/usr/bin/env python3
""" dsv"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """dvd"""

    def __init__(self):
        """dv"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """dv"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """dv"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
