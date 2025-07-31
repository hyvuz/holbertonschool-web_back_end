#!/usr/bin/env python3
"""Return an asyncio.Task for wait_random
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random coroutine.

    Args:
        max_delay (int): maximum delay time

    Returns:
        asyncio.Task: the created Task object
    """
    return asyncio.create_task(wait_random(max_delay))
