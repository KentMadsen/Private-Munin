# Controller
class Business:
    # Initialise Class
    def __init__(self):
        self.continue_work = True
        self.processes = []

    # Work call
    def execute(self):


        return

    # Accessors
    def getContinueWork(self):
        return self.continue_work

    def raiseFlagStop(self):
        self.continue_work = False