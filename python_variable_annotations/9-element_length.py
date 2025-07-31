#!/usr/bin/env python3
"""Defines a function that returns the length of each element in an iterable."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (element, length of element)."""
    return [(i, len(i)) for i in lst]
