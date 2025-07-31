#!/usr/bin/env python3
"""Run multiple task_wait_random concurrently and return their delays
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times and return the list of delays
    in the order they complete.

    Args:
        n (int): number of tasks to run
        max_delay (int): maximum delay value

    Returns:
        List[float]: list of completed delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
