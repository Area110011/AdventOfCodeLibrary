from abc import ABC, abstractmethod
from typing import Optional


class AdventOfCodeTask(ABC):
    def __init__(self):
        self.task_day = 0
        self.task_year = 0
        self.task_input: Optional[str] = None

    def fill(self, task_day: int, task_year: int, task_input: str):
        self.task_day = task_day
        self.task_year = task_year
        self.task_input = task_input

    @abstractmethod
    def run(self):
        pass
