#!/usr/bin/python3
"""
    MRU Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Create a class MRUCache that inherits from BaseCaching"""
    def __init__(self):
        """call the parent init"""
        super().__init__()
        self.key_save = []

    def put(self, key, item):
        """Add an item in the cache using FIFO replacement policy."""
        if key is None or item is None:
            return
        if key in self.key_save:
            self.key_save.remove(key)
        if self.cache_data >= BaseCaching.MAX_ITEMS:
            most_recently = self.key_save.pop()
            del self.cache_data[most_recently]
            print(f"DISCARD: {most_recently}")
        self.key_save.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key and update its usage"""
        if key is None or key in self.cache_data:
            return None

        self.key_save.remove(key)
        self.key_save.append(key)

        return self.cache_data[key]
