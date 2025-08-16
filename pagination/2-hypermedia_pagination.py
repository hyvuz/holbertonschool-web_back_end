#!/usr/bin/env python3
"""Hypermedia pagination over Popular_Baby_Names.csv."""

import csv
import math
from typing import List, Tuple, Dict, Any, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return (start, end) indexes for a 1-indexed page and page_size.

    The end index is exclusive (usable directly for list slicing).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset (list of rows), loading it once."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip header row
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a page of the dataset based on page and page_size.

        Args:
            page: 1-indexed page number (must be positive integer).
            page_size: number of rows per page (must be positive integer).

        Returns:
            A list of rows (each row is a list of strings). Returns an empty
            list if the computed start index is beyond the dataset length.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return hypermedia-style pagination metadata and the page data.

        The dictionary contains:
          - page_size: length of the returned page (0 if out of range)
          - page: current page number
          - data: the list of rows for this page
          - next_page: page + 1 if another page exists, else None
          - prev_page: page - 1 if page > 1, else None
          - total_pages: ceil(total_rows / page_size)
        """
        # Reuse get_page (asserts included there)
        data_page = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        # next_page exists only if current page is strictly before total_pages
        next_page = page + 1 if page < total_pages else None
        # prev_page exists for any page > 1 (even if current page is out of range)
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
