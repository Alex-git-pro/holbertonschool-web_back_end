#!/usr/bin/env python3
"""
Module to run multiple task_wait_random tasks concurrently and return results in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n task_wait_random coroutines with the given max_delay,
    waits for them to complete, and returns a list of delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
