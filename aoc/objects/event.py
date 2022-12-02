from __future__ import annotations

from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from aoc import AdventOfCode, AdventOfCodeTask


class AdventOfCodeEvent:
    registered_tasks = {}

    def __init__(self, instance: AdventOfCode, year: int):
        self.year = year
        self.instance = instance

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.registered_tasks[day] = task

    def execute(self, day: int):
        task_input = self.instance.load_input(day)
        task = self.registered_tasks[day]()

        task.fill(day, self.year, task_input)
        task.run()

    def execute_all(self):
        for day in self.registered_tasks.keys():
            self.execute(day)

    def execute_last(self):
        last_day = list(self.registered_tasks.keys())[-1]

        self.execute(last_day)
