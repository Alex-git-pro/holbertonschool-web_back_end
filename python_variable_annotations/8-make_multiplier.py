#!/usr/bin/env python3
"""Module for make_multiplier function with type annotations."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies its input by multiplier.
    """
    return lambda x: x * multiplier
