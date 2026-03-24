#!/usr/bin/python3
"""Student module with JSON serialization and deserialization."""


class Student:
    """Student class with first_name, last_name, age, to_json, and reload."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in attrs are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from json.

        json is a dictionary with keys as attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
