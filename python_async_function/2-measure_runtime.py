#!/usr/bin/env python3
"""Measure average runtime of wait_n coroutine
"""

import asyncio
from time import perf_counter
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n.

    Args:
        n (int): Number of coroutines to run
        max_delay (int): Maximum delay for each coroutine

    Returns:
        float: Average runtime per coroutine (in seconds)
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return total_time / n
