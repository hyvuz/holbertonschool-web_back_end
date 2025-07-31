#!/usr/bin/env python3
"""Defines a function that returns the floor of a float."""


def floor(n: float) -> int:
    """Return the floor of the float n and handle negative cases."""
    i = int(n)
    if n < 0 and n != i:
        return i - 1
    return i
