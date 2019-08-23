from Source import business, \
                   configuration

# Program boundary
# bootstraps application
# Makes sure everything work
class Application:
    def __init__(self):
        self.business_layer = business.Business()
        self.configuration = configuration.Configuration()

    def initialise(self):
        return None

    def execute(self):
        while self.business_layer.getContinueWork():
            self.business_layer.execute()
        return None

    def garbage(self):
        return None