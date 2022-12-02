from os import path, mkdir
from abc import ABC, abstractmethod
from typing import Optional, Type, List

import requests


class AdventOfCodeConfig:
    debug = False
    testing = False

    auto_fetch_input = False
    cache_input = False

    session: Optional[str] = None

    cache_directory: Optional[str] = None


class AdventOfCodeTask(ABC):
    def __init__(self, task_input: str):
        self.task_input = task_input

    @abstractmethod
    def run(self):
        pass


class AdventOfCodeEvent:
    registered_tasks = {}

    def __init__(self, instance: AdventOfCode):
        # self.year = year
        self.instance = instance

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.registered_tasks[day] = task

    def execute(self, day: int):
        task_input = self.load_input(day)
        task = self.registered_tasks[day](task_input)

        task.run()

    def execute_all(self):
        for day in self.registered_tasks.keys():
            self.execute(day)

    def execute_last(self):
        last_day = list(self.registered_tasks.keys())[-1]

        self.execute(last_day)


class AdventOfCode:
    events: {}
    last_year = 0

    def __init__(self, year: Optional[int] = None):
        self.config = AdventOfCodeConfig()

        if year:
            self.add_year(year)

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

        event = AdventOfCodeEvent()
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
        if not year:
            year = self.last_year

        response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={'session': self.config.session})

        if response.status_code != 200:
            print(f"Failed to fetch input, error: {response.text}")

            return None

        return response.text

    def get_event(self, year: Optional[int] = None):
        if not year:
            year = self.last_year

        return self.events[year]
