from __future__ import annotations

from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from aoc import AdventOfCode, AdventOfCodeTask


class AdventOfCodeEvent:
    def __init__(self, instance: AdventOfCode, year: int):
        self.year = year
        self.instance = instance

        self.registered_tasks = {}

    def register_task(self, day: int, task: Type[AdventOfCodeTask]):
        self.registered_tasks[day] = task

    def execute(self, day: int):
        if self.instance.config.debug:
            print(f"Executing day {day} - year: {self.year}")

        task_input = self.instance.load_input(day)
        task = self.registered_tasks[day]()

        task.fill(day, self.year, task_input)
        task.run()

    def execute_all(self):
        for day in self.registered_tasks.keys():
            self.execute(day)

    def execute_last(self):
        assert self.registered_tasks, f"No tasks added for this event! ({self.year})"

        last_day = list(self.registered_tasks.keys())[-1]

        self.execute(last_day)
