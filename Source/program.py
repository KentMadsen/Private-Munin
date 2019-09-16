from Source.system.application import Application

def main():
    app = Application()

    app.initialise()
    app.execute()

    return app.done()

if __name__ == '__main__':
    print(main())
