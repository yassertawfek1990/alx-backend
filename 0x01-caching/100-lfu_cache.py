#!/usr/bin/env python3
"""rv re"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """rv"""

    def __init__(self):
        """Infd r"""
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """df"""
        if key is None or item is None:
            pass
        else:
            t = len(self.cache_data)
            if t >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                f = min(self.frequency.values())
                f_keys = []
                for a, s in self.frequency.items():
                    if s == f:
                        f_keys.append(a)
                if len(f_keys) > 1:
                    lf = {}
                    for a in f_keys:
                        lf[a] = self.usage.index(a)
                    discard = min(lf.values())
                    discard = self.usage[discard]
                else:
                    discard = f_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            # update
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """df f"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
