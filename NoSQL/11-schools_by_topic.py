#!/usr/bin/env python3
"""Return the list of schools that cover a specific topic."""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Dict[str, Any]]:
    """
    Find all school documents where `topic` is present in the `topics` array.

    Args:
        mongo_collection: pymongo collection object (e.g., client.my_db.school)
        topic: topic to search for (string)

    Returns:
        A list of matching documents (empty list if none).
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
