#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats():
    """Prints the required statistics to stdout (exact format)."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = col.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
