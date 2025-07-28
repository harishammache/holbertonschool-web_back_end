#!/usr/bin/env python3
"""
    writing strings to Redis
"""


import redis
import uuid
from typing import Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """method as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def replay(method: Callable):
        """
        Display the history of calls of a particular function.
        """
        redis_instance = method.__self__._redis
        qualname = method.__qualname__
        calls = int(redis_instance.get(qualname) or 0)
        print(f"{qualname} was called {calls} times:")

        inputs = redis_instance.lrange(f"{qualname}:inputs", 0, -1)
        outputs = redis_instance.lrange(f"{qualname}:outputs", 0, -1)

        for inp, out in zip(inputs, outputs):
            print(f"{qualname}(*{inp.decode()}) -> {out.decode()}")
