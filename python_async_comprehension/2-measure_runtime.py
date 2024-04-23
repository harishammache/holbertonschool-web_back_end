#!/usr/bin/env python3
"""
    Import async_comprehension from the previous file and write
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
"""
import asyncio
from time import perf_counter
from typing import List
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times
    in parallel using asyncio.gather,
    measures the total runtime, and returns it.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()

    total_runtime = end_time - start_time

    return total_runtime
