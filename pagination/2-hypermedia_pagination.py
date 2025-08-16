#!/usr/bin/env python3
"""Hypermedia pagination."""

import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (list of rows), loading it once."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return (start, end) indexes for a 1-indexed page and page_size."""
        end: int = page * page_size
        start: int = 0
        for _ in range(page - 1):
            start += page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page (list of rows) for the given page and page_size."""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        data = self.dataset()
        start, end = self.index_range(page, page_size)

        # match checker behavior: if end extends past dataset, return []
        if end > len(data):
            return []

        # return rows from start to end-1
        return [list(data[i]) for i in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[List[List], None, int]]:
        """Return hypermedia-style pagination metadata and the page data."""
        data_page: List = self.get_page(page, page_size)
        size_dataset: int = len(self.dataset())
        total_pages: int = math.ceil(size_dataset / page_size)

        prev_page = None if page - 1 == 0 else page - 1
        # match checker behavior exactly:
        next_page = None if (page + 1 > size_dataset or data_page == []) \
            else page + 1
        # page_size in the payload is 0 when page is out of range
        payload_page_size = 0 if data_page == [] else page_size

        return {
            'page_size': payload_page_size,
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
