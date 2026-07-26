#!/usr/bin/python3
"""
    This module defines a child class of list.
"""


class VerboseList(list):
    """Inherits list."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, other):
        x = len(other)
        super().extend(other)
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
