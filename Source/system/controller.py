#!/bin/python

class Controller:
    def __init__(self):
        self.continue_work = True
        self.services = []

    def execute(self):
        while self.continue_work:
            for i in range(len(self.services)):
                selected = self.services[i]

        return None

    def add_server(self, service):
        self.services.append(service)
        return