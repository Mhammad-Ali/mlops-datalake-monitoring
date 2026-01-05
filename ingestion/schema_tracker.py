import json
import os

SCHEMA_FILE = "ingestion/last_schema.json"

def load_last_schema():
    if os.path.exists(SCHEMA_FILE):
        with open(SCHEMA_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_schema(schema_features):
    with open(SCHEMA_FILE, "w") as f:
        json.dump(list(schema_features), f)

def compare_schema(new_schema_features):
    old_schema = load_last_schema()

    added = new_schema_features - old_schema
    removed = old_schema - new_schema

    return added, removed
