#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

This module defines an async routine that runs multiple coroutines concurrently
and returns their results in order of completion.

Author: [Your Name]
"""

import asyncio
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Returns a list of delays in the order they were completed.

    Args:
        n (int): Number of times to call wait_random
        max_delay (int): Maximum delay value for wait_random

    Returns:
        List[float]: List of delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
