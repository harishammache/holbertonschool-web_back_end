#!/usr/bin/python3
"""
    LRU Caching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Create a class LRUCache that inherits from BaseCaching"""
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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.key_save.pop(0)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.key_save.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key."""
        if key is None or key not in self.cache_data:
            return None
        self.key_save.remove(key)
        self.key_save.append(key)
        return self.cache_data.get(key)
