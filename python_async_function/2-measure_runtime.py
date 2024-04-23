#!/usr/bin/env python3
"""
    Measure the runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        function: measure_time

        arguments: n and max_delay who are an int

        return: float
    """
    start_time = time.time()
    formatted_time_start = time.ctime(start_time)
    print(formatted_time_start)

    result = asyncio.run(wait_n(n, max_delay))
    print(result)

    end_time = time.time()
    formatted_time_end = time.ctime(end_time)
    print(formatted_time_end)

    total_time = end_time - start_time
    average_time_per_call = total_time / n

    return average_time_per_call
