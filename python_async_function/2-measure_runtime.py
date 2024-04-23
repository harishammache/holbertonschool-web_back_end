#!/usr/bin/env python3
"""
    Measure the runtime
"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import asyncio



def measure_time(n: int, max_delay: int) -> float:
    """
        function: measure_time

        arguments: n and max_delay who are an int

        return: float
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_call = total_time / n

    return average_time_per_call
