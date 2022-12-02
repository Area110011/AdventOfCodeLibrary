from aoc import AdventOfCode, AdventOfCodeTask


task_executed = False


class TestTask(AdventOfCodeTask):
    def run(self):
        global task_executed
        task_executed = True


def test_aoc():
    instance = AdventOfCode(2022)
    instance.register_task(1, TestTask)

    instance.execute(1)

    assert task_executed, "Failed to execute test task!"
