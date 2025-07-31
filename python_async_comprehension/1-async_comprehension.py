#!/usr/bin/env python3
"""async_comprehension module

This module defines a coroutine that uses async comprehension
to collect 10 random float numbers from an asynchronous generator.
"""

import asyncio
from typing import List

# Import the async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random float numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 float numbers generated asynchronously.
    """
    return [n async for n in async_generator()]
