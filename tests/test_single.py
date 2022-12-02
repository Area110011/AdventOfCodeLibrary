from aoc import AdventOfCode, AdventOfCodeTask

current_task = 0
executed_tasks = 0


class TestTask(AdventOfCodeTask):
    def run(self):
        if current_task != 0:
            assert current_task == self.task_day, "Wrong day executed!"

        global executed_tasks
        executed_tasks += 1


def test_aoc():
    global current_task

    instance = AdventOfCode(2022)
    instance.register_task(1, TestTask)
    instance.register_task(2, TestTask)
    instance.register_task(3, TestTask)

    # Mark instance as testing to supply dummy input
    instance.config.testing = True

    instance.execute(current_task := 1)
    instance.execute(current_task := 2)
    instance.execute(current_task := 3)

    instance.register_task(4, TestTask)

    current_task = 4
    instance.execute_last()

    global executed_tasks
    assert executed_tasks == 4, "Wrong amount of tasks has been executed!"

    current_task = 0
    executed_tasks = 0

    instance.execute_all()
    assert executed_tasks == 4, "Wrong amount of tasks has been executed!"
