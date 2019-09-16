#!/bin/bash
from Source.system.parsers.configuration_parser import ConfigurationParser

import os, sys


cfg_paths = '\configuration'

class Configuration:
    def __init__(self, v_controller):
        self.controller = v_controller
        self.current_program_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.configuration_path = self.current_program_path + cfg_paths

        self.configuration_files = []

    def run(self):
        print( 'Configuration Executing' )

        for r, d, f in os.walk( self.configuration_path ):
            for file in f:
                if '.cfg' in file:
                    self.configuration_files.append( os.path.join( r, file ) )

        self.open_configuration_files()

        return

    def open_configuration_files(self):

        for i in range(len(self.configuration_files)):
            currently_selected = self.configuration_files[i]

            self.open_configuration_file(currently_selected)

        return

    def open_configuration_file(self, file_path):
        print("Selected configuration file: " + file_path)

        parser = ConfigurationParser(file_path)

        parser.open()

        parser.parse()

        parser.done()

        return

