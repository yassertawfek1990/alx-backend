#!/usr/bin/env python3
'''fd f'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A cldfv'''

    def put(self, key, item):
        '''dsvf'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''rdsv'''

        return self.cache_data.get(key, None)
