#!/usr/bin/python3
"""
    This module defines a new iterator class.
"""


class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0


    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count