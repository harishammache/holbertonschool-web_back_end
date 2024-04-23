#!/usr/bin/env python3
"""
    1. Let's execute multiple coroutines at the same time with async
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        fonction wait_n

        two arguments: n and max_delay who are an int

        return a float
    """
    list_delay = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        list_delay.append(delay)
    return sorted(list_delay)

if __name__ == "__main__":
    wait = wait_n(2, 10)
    print(asyncio.run(wait))
