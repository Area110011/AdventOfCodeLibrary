from __future__ import annotations

from typing import Optional, Type, TYPE_CHECKING
from typing_extensions import Unpack

from .helper import EventExecuteArgs, TaskParameters

if TYPE_CHECKING:
    from aoc import AdventOfCode, AdventOfCodeTask


class AdventOfCodeEvent:
    def __init__(self, instance: AdventOfCode, year: int):
        self.year = year
        self.instance = instance

        self.registered_tasks = {}

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.registered_tasks[day] = task

    def execute(self, day: int, **kwargs: Unpack[EventExecuteArgs]):
        if self.instance.config.debug:
            print(f"Executing day {day} - year: {self.year}")

        # self.__check_no_tasks()
        assert day in self.registered_tasks, f"Task for {day}. day is not registered!"

        task_input = self.instance.load_input(day, self.year)
        task = self.registered_tasks[day]()

        task.execute(kwargs.get('variant'), TaskParameters(day, self.year, task_input))

    def execute_all(self, **kwargs: Unpack[EventExecuteArgs]):
        self.__check_no_tasks()

        for day in self.registered_tasks.keys():
            self.execute(day, **kwargs)

    def execute_last(self, **kwargs: Unpack[EventExecuteArgs]):
        self.__check_no_tasks()

        last_day = list(self.registered_tasks.keys())[-1]

        self.execute(last_day, **kwargs)

    def __check_no_tasks(self):
        assert self.registered_tasks, f"No tasks added for this event! ({self.year})"
