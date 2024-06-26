#!/usr/bin/python3
"""dfv"""


class BaseCaching():
    """dfv r"""
    MAX_ITEMS = 4

    def __init__(self):
        """sgf"""
        self.cache_data = {}

    def print_cache(self):
        """dfv"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """dsfv f"""
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """sg g"""
        raise NotImplementedError("get must be implemented in your cache class")
