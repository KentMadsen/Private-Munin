#!/bin/python
# LIBRARY [COMPILER:COLLECT]
# DEPENDENCY [COMPILER:COLLECT]
# ---------------------------------------------------------------------------------------------------------------------

# DEPENDENCY [COMPILER:BEGIN]
from Source.system.application import Application
# DEPENDENCY [COMPILER:END]

def main():
    app = Application()

    app.initialise()
    app.execute()

    return app.done()

if __name__ == '__main__':
    print(main())
