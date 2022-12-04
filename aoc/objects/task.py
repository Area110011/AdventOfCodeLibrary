from abc import ABC, abstractmethod
from typing import Type, Optional

from .helper import TaskParameters


class AdventOfCodeTaskVariant(ABC):
    # noinspection PyAttributeOutsideInit
    def setup(self, parameters: TaskParameters):  # __setup
        self.parameters = parameters

    @abstractmethod
    def run(self):
        pass


class AdventOfCodeTask(AdventOfCodeTaskVariant):
    def add_variant(self, index: int, variant: Type[AdventOfCodeTaskVariant]):
        self.__check_index(index)
        self.__check_variants()

        self.variants[index] = variant

    def execute(self, index: Optional[int], parameters: TaskParameters):
        self.__check_index(index)
        self.__check_variants()

        if index is None:
            self.setup(parameters)
            self.run()

            return

        assert index in self.variants, f"No variant for index {index} is added!"

        variant = self.variants[index]()
        parameters.set_variant(index)

        variant.setup(parameters)
        variant.run()

    def run(self):
        pass

    # noinspection PyMethodMayBeStatic
    def __check_index(self, index: int):
        if index is None:
            return

        assert index >= 0, "Variant index cannot be negative!"

    # noinspection PyUnresolvedReferences
    def __check_variants(self):
        if not hasattr(self, 'variants'):
            self.variants = {}
