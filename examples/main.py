from aoc import AdventOfCode, AdventOfCodeTask


class ExampleTask(AdventOfCodeTask):
    def run(self):
        # This method is called on execute
        pass


def main():
    instance = AdventOfCode(2022)  # Create instance of library with current year
    instance.enable_auto_input_fetch("<session_token>")  # We can enable auto fetching input, session token can be obtained from browser cookies
    instance.enable_auto_input_fetch("<session_token>", True)  # Also we can enable caching for these requests, it will download input to cache folder and use it on next run
    instance.enable_auto_input_fetch("<session_token>", True, "/temp")  # Cache directory can be changed by third parameter, '/' means working folder

    instance.register_task(1, ExampleTask)  # Register task to specific day

    instance.execute(1)  # Now we can execute task on that day by running this command, this will call run() method in task class
    instance.execute_all()  # This is the same as above, but it will run all days one by one
    instance.execute_last()  # This will execute only last day task that was added


if __name__ == '__main__':
    main()
