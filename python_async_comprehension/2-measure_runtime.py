#!/usr/bin/env python3
"""measure_runtime module
"""

import asyncio
import time
from typing import Callable

# Import the async_comprehension coroutine from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total time taken to run all comprehensions.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    return end_time - start_time
