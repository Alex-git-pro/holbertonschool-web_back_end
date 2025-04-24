#!/usr/bin/env python3
"""Module for to_kv function with type annotations."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float.

    Args:
        k (str): A string key.
        v (Union[int, float]): A numeric value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string,
        and the second is the square of the number as a float.
    """
    return (k, float(v ** 2))
