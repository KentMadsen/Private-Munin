#!/bin/python

class Counter:
    def __init__(self):
        self.i = 0

    # Function
    def increase(self, a):
        self.i = self.i + a

    def increment(self):
        self.increase( 1 )

    def decrease(self, d):
        self.i = self.i - d

    def decrement(self):
        self.decrease( 1 )

    # Accessors
    def getValue(self):
        return self.i

    def setValue(self, a):
        self.i = a