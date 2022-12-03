from __future__ import annotations

from os import path, mkdir
from typing import Optional, Type, TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from aoc import AdventOfCodeEvent, AdventOfCodeTask


class AdventOfCodeConfig:
    def __init__(self):
        self.debug = False
        self.testing = False

        self.auto_fetch_input = False
        self.cache_input = False

        self.session: Optional[str] = None

        self.cache_directory: Optional[str] = None


class AdventOfCode:
    def __init__(self, year: Optional[int] = None):
        self.config = AdventOfCodeConfig()

        self.events = {}
        self.last_year = 0
        self.manual_input: Optional[str] = None

        if year:
            self.add_year(year)

    def enable_debug(self):
        self.config.debug = True

    def enable_auto_input_fetch(self, session: str, cache: bool = False, cache_directory: str = "/cache"):
        self.config.session = session
        self.config.auto_fetch_input = True

        if cache:
            self.config.cache_directory = cache_directory
            self.config.cache_input = cache

            if not path.exists(self.config.cache_directory):
                mkdir(self.config.cache_directory)

    def add_year(self, year: int) -> AdventOfCodeEvent:
        self.last_year = year

        from aoc import AdventOfCodeEvent
        event = AdventOfCodeEvent(self, year)
        self.events[year] = event

        return event

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.events[self.last_year].register_task(day, task)

    def execute(self, day: int, year: Optional[int] = None):
        event = self.get_event(year)
        event.execute(day)

    def execute_all(self, year: Optional[int] = None):
        event = self.get_event(year)
        event.execute_all()

    def execute_last(self, year: Optional[int] = None):
        event = self.get_event(year)
        event.execute_last()

    def load_input(self, day: int, year: Optional[int] = None) -> Optional[str]:
        if self.config.testing:
            return "Dummy"

        if self.manual_input:
            return self.manual_input

        if not year:
            year = self.last_year

        task_input = None
        cache_file = None

        if self.config.cache_input:
            cache_file = path.join(self.config.cache_directory, f"{year}-{day}.tmp")

            if path.exists(cache_file):
                with open(cache_file, "r") as file:
                    task_input = file.read()

        if not task_input:
            task_input = self.fetch_input(day, year)

            if self.config.cache_input:
                with open(cache_file, "w") as file:
                    file.write(task_input)

        return task_input

    def fetch_input(self, day: int, year: Optional[int] = None) -> Optional[str]:
        # if not self.config.auto_fetch_input:
        #    return None

        assert self.config.auto_fetch_input, "Automatic fetching of input is disabled, enable it using 'enable_auto_input_fetch' or set manually input by 'set_input'!"

        if not year:
            year = self.last_year

        url = f"https://adventofcode.com/{year}/day/{day}/input"

        if self.config.debug:
            print(f"Fetching input from {url}")

        response = requests.get(url, cookies={'session': self.config.session})

        if response.status_code != 200:
            print(f"Failed to fetch input, error: {response.text}")

            return None

        return response.text

    def get_event(self, year: Optional[int] = None):
        if not year:
            year = self.last_year

        return self.events[year]

    def set_input(self, manual_input: str):
        self.manual_input = manual_input
