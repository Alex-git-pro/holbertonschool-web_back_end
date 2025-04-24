#!/usr/bin/env python3
"""
Module to run multiple coroutines concurrently and return the results in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently with the given max_delay.
    
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay to be passed to wait_random.
    
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    for coroutine in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coroutine
        delays.append(delay)
    return delays
