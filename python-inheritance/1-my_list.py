#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """This class inherits from the built-in list class."""

    def print_sorted(self):
        """This method prints the list in ascending sorted order."""
        print(sorted(self))
