#!/usr/bin/env python3
"""Simple pagination over Popular_Baby_Names.csv."""

import csv
from typing import List, Tuple


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
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset (list of rows), loading it once."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header row
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
