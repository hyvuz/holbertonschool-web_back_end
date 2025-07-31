#!/usr/bin/env python3
"""async_generator module

This module defines an asynchronous generator function
that yields 10 random float numbers between 0 and 10,
pausing for 1 second between each.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random float numbers.

    Each value is generated after a 1-second asynchronous delay.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
