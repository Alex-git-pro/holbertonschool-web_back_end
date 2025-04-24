#!/usr/bin/env python3
"""Module for element_length function with type annotations."""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.

    Each tuple contains the sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like items.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples (sequence, length).
    """
    return [(i, len(i)) for i in lst]
