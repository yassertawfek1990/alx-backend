#!/usr/bin/env python3

'''Task 0: Basic dictionary sdj asc awdqwm aesck
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A cldfv wenclkwenclk eckkl clkwec '''

    def put(self, key, item):
        '''dsvf wjnkln cewkcklewvv welckm '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''rdsv knlkwec klkewc m 
        ewklckl e
        ml;m;lm ewc'''

        return self.cache_data.get(key, None)
