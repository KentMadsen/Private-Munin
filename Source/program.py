from Source import application

def main():
    app = application.Application()

    app.initialise()
    app.execute()

    return app.garbage()

if __name__ == '__main__':
    print(main())
