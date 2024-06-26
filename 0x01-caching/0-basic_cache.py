#!/usr/bin/env python3
'''dsv'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''sdv s'''
    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''dsv'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''rsd'''
        return self.cache_data.get(key, None)
