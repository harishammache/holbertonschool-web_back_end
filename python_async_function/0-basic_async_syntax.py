#!/usr/bin/env python3
"""
    0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds.

    Parameters:
        max_delay (int, optional): The maximum delay in seconds (default is 10)

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    wait = wait_random(10)
    print(asyncio.run(wait))