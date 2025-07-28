#!/usr/bin/env python3
"""
    writing strings to Redis
"""


import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key, fn: Optional[Callable]):
        """method that take a key string argument"""
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def to_str(self, data: bytes) -> str:
        """methode to_str"""
        return data.decode()

    def to_int(self, data: bytes) -> int:
        """methode to_int"""
        return int(data.decode())

    def get_str(self, key: str) -> Optional[str]:
        """methode get_str"""
        return self.get(key, self.to_str)

    def get_int(self, key: str) -> Optional[int]:
        """methode get_int"""
        return self.get(key, self.to_int)
