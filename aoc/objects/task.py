from abc import ABC, abstractmethod


class AdventOfCodeTask(ABC):
    # noinspection PyAttributeOutsideInit
    def fill(self, task_day: int, task_year: int, task_input: str):
        self.task_day = task_day
        self.task_year = task_year
        self.task_input = task_input

    @abstractmethod
    def run(self):
        pass
