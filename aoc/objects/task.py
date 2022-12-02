from abc import ABC, abstractmethod


class AdventOfCodeTask(ABC):
    def __init__(self, task_input: str):
        self.task_input = task_input

    @abstractmethod
    def run(self):
        pass
