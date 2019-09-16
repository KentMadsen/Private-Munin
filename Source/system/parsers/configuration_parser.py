#!/bin/python
class ConfigurationParser:
    def __init__(self, cfg_path):
        self.path = cfg_path

        self.file = None

    def open(self):
        self.file = open(self.path, "r")
        return

    def parse(self):
        fl = self.file.readlines()

        for line in fl:
            print( line, end='' )

        print()

        return

    def done(self):
        self.file.close()
        return