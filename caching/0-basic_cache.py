#!/usr/bin/python3
"""
    Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits from BaseCaching"""
    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
