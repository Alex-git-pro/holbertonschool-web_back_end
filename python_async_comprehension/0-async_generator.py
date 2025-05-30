#!/usr/bin/env python3
"""
Coroutine called async_generator that takes no arguments.
"""

from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.

    Yields:
        Float: Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
