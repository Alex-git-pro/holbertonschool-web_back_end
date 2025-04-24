#!/usr/bin/env python3
"""
Module contains a coroutine that delays for a random amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
