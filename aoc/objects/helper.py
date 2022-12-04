from typing import TypedDict


class LibraryExecuteArgs(TypedDict):
    year: int
    variant: int


class EventExecuteArgs(TypedDict):
    variant: int


class TaskParameters(object):
    def __init__(self, day: int, year: int, input: str):
        self.day = day
        self.year = year
        self.input = input

        self.variant = None

    def set_variant(self, variant: int):
        self.variant = variant
