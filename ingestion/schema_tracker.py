# ingestion/schema_tracker.py

import json
import os
from monitoring.metrics import increment

SCHEMA_FILE = "schema.json"

def track_schema(new_record: dict):
    new_schema = set(new_record.keys())

    if not os.path.exists(SCHEMA_FILE):
        with open(SCHEMA_FILE, "w") as f:
            json.dump(list(new_schema), f)
        return

    with open(SCHEMA_FILE, "r") as f:
        old_schema = set(json.load(f))

    added = new_schema - old_schema
    removed = old_schema - new_schema

    if added:
        increment("feature_added", len(added))
        print("➕ Features added:", added)

    if removed:
        increment("feature_removed", len(removed))
        print("➖ Features removed:", removed)

    if added or removed:
        with open(SCHEMA_FILE, "w") as f:
            json.dump(list(new_schema), f)
