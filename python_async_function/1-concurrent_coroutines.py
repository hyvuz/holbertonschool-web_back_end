#!/usr/bin/env python3
"""wait n times module
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random concurrently n times.

    Args:
        n (int): number of times to run wait_random
        max_delay (int): maximum delay time

    Returns:
        List[float]: list of delays in order of completion
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
