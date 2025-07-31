#!/usr/bin/env python3
"""

This module defines an asynchronous coroutine that waits
for a random delay and returns the delay value.

Author: [Your Name]
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive) and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual random delay used.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
