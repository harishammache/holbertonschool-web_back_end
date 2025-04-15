#!/usr/bin/bash
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Create a class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """call the parent init"""
        super().__init__()
        self.key_save = []
    
    def put(self, key, item):
        """Add an item in the cache using FIFO replacement policy."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.key_save.pop()
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.key_save.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
    
        
