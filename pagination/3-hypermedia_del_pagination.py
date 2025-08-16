#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
import math  # kept to match the provided starter; not required by the logic
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List]] = None
        self.__indexed_dataset: Optional[Dict[int, List]] = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (list of rows), loading it once."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip header row.
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return a dict mapping row index to row, starting at 0.

        The dict may become sparse if rows are removed.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # The starter snippet mentions a truncated slice, but builds the full index.
            truncated_dataset = dataset[:1000]  # kept to mirror the provided starter
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page anchored at a given start index.

        The page is built by walking forward from `index` and collecting up to
        `page_size` existing rows in the indexed dataset (skipping deleted keys).

        Returns a dict with:
          - index: the requested start index (anchor).
          - next_index: the first index to request after this page.
          - page_size: the number of rows actually returned.
          - data: the list of rows for this page.
        """
        # Default behavior: if index is not provided, start at 0.
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        idx_data = self.indexed_dataset()
        # Validate range against current index size (as in the Holberton checker).
        assert index < len(idx_data)

        data: List[List] = []
        collected = 0
        i = index
        max_key = max(idx_data.keys()) if idx_data else -1

        # Walk forward, skipping holes, until we collect `page_size` rows or run out.
        while collected < page_size and i <= max_key:
            row = idx_data.get(i)
            if row is not None:
                data.append(row)
                collected += 1
            i += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": i,
        }
