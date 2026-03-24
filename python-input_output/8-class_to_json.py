#!/usr/bin/python3
"""Return dictionary description of a class for JSON serialization."""


def class_to_json(obj):
    """Return dictionary representation of a class instance."""
    return obj.__dict__.copy()
