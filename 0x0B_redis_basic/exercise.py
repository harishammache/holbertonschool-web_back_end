#!/usr/bin/env python3
"""
    writing strings to Redis
"""


import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """method, store an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """method that takes a data argument and returns a string"""
        key = str(uuid.uuid4())

        if isinstance(data, str):
            data = data.encode('utf-8')

        elif isinstance(data, (int, float)):
            data = str(data).encode('utf-8')

        self._redis.set(key, data)

        return key
