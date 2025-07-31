#!/usr/bin/env python3
"""
0-async_generator.py

This module defines an asynchronous generator function
that yields 10 random float numbers between 0 and 10,
with a 1-second pause between each value.

Used to demonstrate asynchronous generators and `async for` usage.
"""

import asyncio
import random

async def async_generator():
    """
    Coroutine that yields 10 random numbers asynchronously.

    Each iteration:
    - Waits asynchronously for 1 second using asyncio.sleep
    - Yields a random float number between 0 and 10 (inclusive)

    Yields:
        float: A random float number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
