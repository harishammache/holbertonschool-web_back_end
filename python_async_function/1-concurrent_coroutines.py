#!/usr/bin/env python3
"""
    1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
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
