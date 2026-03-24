#!/usr/bin/env python3
"""Module that extends list with notifications"""


class VerboseList(list):
    """A list that prints messages when modified"""

    def append(self, item):
        """Add item to list and print message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend list and print message"""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item from list and print message"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print message"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
