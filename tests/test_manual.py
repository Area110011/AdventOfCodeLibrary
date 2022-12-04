from aoc import AdventOfCode, AdventOfCodeTask, AdventOfCodeTaskVariant


class TestTaskFirstVariant(AdventOfCodeTaskVariant):
    def run(self):
        print(f"First Variant")
        print(f"- Parameters: {self.parameters.__dict__}")


class TestTaskSecondVariant(AdventOfCodeTaskVariant):
    def run(self):
        print(f"Second Variant")
        print(f"- Parameters: {self.parameters.__dict__}")


class TestTask(AdventOfCodeTask):
    def __init__(self):
        self.add_variant(0, TestTaskFirstVariant)
        self.add_variant(1, TestTaskSecondVariant)

    def run(self):
        print(f"Third Variant")
        print(f"- Parameters: {self.parameters.__dict__}")


def main():
    instance = AdventOfCode(2022)
    instance.set_input("Hello, world!")

    instance.register_task(1, TestTask)

    instance.execute(1)


if __name__ == '__main__':
    main()
