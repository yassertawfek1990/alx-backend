#!/usr/bin/env python3
"""gfjhbdsjhvc hj jhjhjsdbcjhb jhdsg"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """fg,jhjhb,jhsdc kj klnlkjn sdckj"""

    def __init__(self):
        """fgjbkjb sdc kjkjn kj dsc"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """gf gf.jbkj kjn sdakc jknkln;kn ;kl asdcnkjnl lksdv"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """fv gfhbskljd cbkjb kjls dkljbc kjlb asdlkjcj klsjd"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
