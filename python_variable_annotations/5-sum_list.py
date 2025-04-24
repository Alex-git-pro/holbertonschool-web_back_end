#!/usr/bin/env python3
"""Module for sum_list function with type annotations."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(input_list)
