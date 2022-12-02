from aoc import AdventOfCode, AdventOfCodeTask


class ExampleTask(AdventOfCodeTask):
    def run(self):
        # This method is called on execute
        pass


def main():
    #
    # Single event usage
    #
    instance = AdventOfCode(2022)  # Create instance with current event

    instance.register_task(1, ExampleTask)  # Register task to specific day

    instance.execute(1)  # Now we can execute task on that day by running this command, this will call run() method in task class
    instance.execute_all()  # This is the same as above, but it will run all days one by one
    instance.execute_last()  # This will execute only last day task that was added

    #
    # Multiple events usage
    #
    instance = AdventOfCode()  # Create instance with no events, we'll need to add events later
    instance = AdventOfCode(2015)  # Create instance with predefined event

    instance.register_task(1, ExampleTask)  # This task will be added to 2015 event

    instance.add_year(2020)  # This will create 2020 event and all execution of 'register_task' will add days to this event

    instance.register_task(1, ExampleTask)  # This task will be added to 2020 event

    # Registering using event instance
    event = instance.add_year(2018)  # This will create 2018 event and returns instance of that event. This can be used to add tasks directly to specific event

    event.register_task(1, ExampleTask)  # This task will be added to instance of 2018 event

    # Execution
    instance.execute(1)  # This will execute first day of last event (in our case 2018 event)
    instance.execute(1, 2015)  # This will execute first day of 2015 event

    instance.execute_last()  # This will execute last day (1) of last event (2018)
    instance.execute(2015)  # This will execute last day of 2015 event

    instance.execute_all()  # This will execute all days one by one in last event (2018)
    instance.execute_all(2015)  # This will execute all days one by one in 2015 event

    #
    # Shared usage
    # This will usually be enabled after initializing instance of library
    #

    instance.enable_auto_input_fetch("<session_token>")  # We can enable auto fetching input, session token can be obtained from browser cookies
    instance.enable_auto_input_fetch("<session_token>", True)  # Also we can enable caching for these requests, it will download input to cache folder and use it on next run
    instance.enable_auto_input_fetch("<session_token>", True, "/temp")  # Cache directory can be changed by third parameter, '/' means working folder


if __name__ == '__main__':
    main()
