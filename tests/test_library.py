from aoc import AdventOfCode, AdventOfCodeTask


first_task_executed = False
second_task_executed = False
third_task_executed = False
last_task_executed = False

executed_tasks = 0


class FirstTestTask(AdventOfCodeTask):
    def run(self):
        global first_task_executed, executed_tasks
        first_task_executed = True
        executed_tasks += 1


class SecondTestTask(AdventOfCodeTask):
    def run(self):
        global second_task_executed, executed_tasks
        second_task_executed = True
        executed_tasks += 1


class ThirdTestTask(AdventOfCodeTask):
    def run(self):
        global third_task_executed, executed_tasks
        third_task_executed = True
        executed_tasks += 1


class LastTestTask(AdventOfCodeTask):
    def run(self):
        global last_task_executed, executed_tasks
        last_task_executed = True
        executed_tasks += 1


def test_aoc():
    instance = AdventOfCode(2022)
    instance.register_task(1, FirstTestTask)
    instance.register_task(2, SecondTestTask)
    instance.register_task(3, ThirdTestTask)

    # Mark instance as testing to supply dummy input
    instance.config.testing = True

    instance.execute(1)
    assert first_task_executed, "Failed to execute first test task!"
    instance.execute(2)
    assert second_task_executed, "Failed to execute second test task!"
    instance.execute(3)
    assert third_task_executed, "Failed to execute third test task!"

    instance.register_task(4, LastTestTask)

    instance.execute_last()
    # assert last_task_executed, "Failed to execute last test task!"

    global executed_tasks
    assert executed_tasks == 3, "Wrong amount of tasks has been executed!"  # Modify to 4 when execute_last will work

    executed_tasks = 0

    instance.execute_all()
    assert executed_tasks == 4, "Wrong amount of tasks has been executed!"
