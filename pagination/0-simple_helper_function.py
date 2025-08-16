#!/usr/bin/env python3
"""
Module for calculating start and end indexes for pagination
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes
    for the given page and page_size.

    Args:
    page (int): The current page number (1-indexed).
    page_size (int): Number of items per page.

    Returns:
    Tuple[int, int]: A tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
  
