#!/bin/python

# DEPENDENCY [COMPILER:BEGIN]
from Source.system.controller import Controller
from Source.system.configuration import Configuration
# DEPENDENCY [COMPILER:END]


class Application:
    def __init__(self):
        self.controller = Controller()
        self.configuration = Configuration(self.controller)
        self.output = "Application is done"

    def initialise(self):
        print("Initialisation")
        self.configuration.run()
        return

    def execute(self):
        print("Execution")
        self.controller.execute()
        return

    def done(self):
        return self.output
