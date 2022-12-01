from os import path, mkdir
from abc import ABC, abstractmethod
from typing import Optional, Type

import requests


class AdventOfCodeConfig:
    debug = False

    auto_fetch_input = False
    cache_input = False

    session: Optional[str] = None

    cache_directory: Optional[str] = None

    def __init__(self, year):
        self.year = year


class AdventOfCodeTask(ABC):
    def __init__(self, input: str):
        self.input = input

    @abstractmethod
    def run(self):
        pass


class AdventOfCode:
    registered_tasks = {}

    def __init__(self, year: int):
        self.config = AdventOfCodeConfig(year)

    def enable_auto_input_fetch(self, session: str, cache: bool = False, cache_directory: str = "/cache"):
        self.config.session = session
        self.config.auto_fetch_input = True

        if cache:
            self.config.cache_directory = cache_directory
            self.config.cache_input = cache

            if not path.exists(self.config.cache_directory):
                mkdir(self.config.cache_directory)

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.registered_tasks[day] = task

    def execute(self, day: int):
        input = self.load_input(day)
        task = self.registered_tasks[day](input)

        task.run()

    def execute_all(self):
        pass

    def execute_last(self):
        pass

    def load_input(self, day: int):
        input = None
        cache_file = None

        if self.config.cache_input:
            cache_file = path.join(self.config.cache_directory, f"{day}.tmp")

            if path.exists(cache_file):
                with open(cache_file, "r") as file:
                    input = file.read()

                if self.config.debug:
                    print(f"input {day} loaded")

        if not input:
            input = self.fetch_input(day)

            if self.config.cache_input:
                with open(cache_file, "w") as file:
                    file.write(input)

                if self.config.debug:
                    print(f"input {day} cached")

        return input

    def fetch_input(self, day: int) -> Optional[str]:
        response = requests.get(f"https://adventofcode.com/{self.config.year}/day/{day}/input", cookies={'session': self.config.session})

        if response.status_code != 200:
            print(f"Failed to fetch input, error: {response.text}")

            return None

        if self.config.debug:
            print(f"input {day} fetched")

        return response.text
