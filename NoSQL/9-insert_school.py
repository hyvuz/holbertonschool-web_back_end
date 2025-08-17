#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection based on kwargs."""
from typing import Any, Dict


def insert_school(mongo_collection, **kwargs) -> Any:
    """
    Inserts a document in the given collection using keyword arguments.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Fields/values for the new document (e.g., name="UCSF").

    Returns:
        The ObjectId of the newly inserted document.
    """
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id
