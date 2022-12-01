from os import path, mkdir
from abc import ABC, abstractmethod
from typing import Optional, Type

import requests


class AdventOfCodeConfig:
    auto_fetch_input = False
    cache_input = False

    session: Optional[str] = None

    cache_directory: Optional[str] = None

    def __init__(self, year):
        self.year = year


class AdventOfCodeTask(ABC):
    @abstractmethod
    def run(self):
        pass


class AdventOfCode:
    def __init__(self, year: int, main_file: str):
        self.config = AdventOfCodeConfig(year)
        self.main_file = main_file

    def enable_auto_input_fetch(self, session: str, cache: bool = False):
        self.config.session = session
        self.config.auto_fetch_input = True
        self.config.cache_input = cache

        if cache:
            self.config.cache_directory = path.join(path.dirname(self.main_file), "cache")

            if not path.exists(self.config.cache_directory):
                mkdir(self.config.cache_directory)

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        pass

    def execute(self, day: int):
        input = self.load_input(day)

    def execute_all(self):
        pass

    def load_input(self, day: int):
        input = None
        cache_file = None

        if self.config.cache_input:
            cache_file = path.join(self.config.cache_directory, f"{day}.tmp")

            if path.exists(cache_file):
                with open(cache_file, "r") as file:
                    input = file.read()

                print(f"input {day} loaded")

        if not input:
            input = self.fetch_input(day)

            if self.config.cache_input:
                with open(cache_file, "w") as file:
                    file.write(input)

                print(f"input {day} cached")

        return input

    def fetch_input(self, day: int) -> Optional[str]:
        response = requests.get(f"https://adventofcode.com/{self.config.year}/day/{day}/input", cookies={'session': self.config.session})

        if response.status_code != 200:
            print(f"Failed to fetch input, error: {response.text}")

            return None

        print(f"input {day} fetched")

        return response.text