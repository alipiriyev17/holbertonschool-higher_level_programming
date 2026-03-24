#!/usr/bin/env python3
"""Module that implements a counted iterator"""


class CountedIterator:
    """Iterator that counts how many items were iterated"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
