#!/usr/bin/env python3

'''Task 0: Basic dictionary sdj asc awdqwm aesck
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A cldfv wenclkwenclk eckkl clkwec '''

    def __init__(self):
        """
        Initialize the class ds s dsvusing the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''dsvf wjnkln cewkcklewvv welckm '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''rdsv knlkwec klkewc m
        ewklckl e
        ml;m;lm ewc'''

        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
