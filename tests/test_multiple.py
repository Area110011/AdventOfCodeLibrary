from aoc import AdventOfCode, AdventOfCodeTask

current_day = 0
current_year = 0

executed_tasks = 0


class TestTask(AdventOfCodeTask):
    def run(self):
        if current_day != 0:
            assert current_day == self.task_day, "Wrong day executed!"
        if current_year != 0:
            assert current_year == self.task_year, "Wrong year executed!"

        global executed_tasks
        executed_tasks += 1


def add_year(instance: AdventOfCode, year: int):
    instance.add_year(year)

    for i in range(1, 4):
        instance.register_task(i, TestTask)


def add_year_event(instance: AdventOfCode, year: int):
    event = instance.add_year(year)

    for i in range(1, 4):
        event.register_task(i, TestTask)


def execute_year(instance: AdventOfCode, year: int):
    global current_year
    current_year = year

    global current_day

    for i in range(1, 4):
        current_day = i
        instance.execute(i, year)

    global executed_tasks
    assert executed_tasks == 3, "Wrong amount of tasks has been executed!"
    executed_tasks = 0


def test_aoc():
    instance = AdventOfCode()

    # Mark instance as testing to supply dummy input
    instance.config.testing = True

    # Adding by last year
    for i in range(2015, 2018):
        add_year(instance, i)

    # Adding using event instance
    for i in range(2022, 2019, -1):
        add_year_event(instance, i)

    # Executing
    for i in range(2015, 2018):
        execute_year(instance, i)

    for i in range(2022, 2019, -1):
        execute_year(instance, i)
