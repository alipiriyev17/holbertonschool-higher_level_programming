#!/usr/bin/python3
"""Basic serialization module.

Provides functions to serialize a Python dictionary to a JSON file and
deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON file name. Existing file will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it to a Python dictionary.

    Args:
        filename (str): Input JSON file name.

    Returns:
        dict: Python dictionary deserialized from JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
