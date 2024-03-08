class Pycharm:
    def execute(self):
        print("Running")
        print("Executing")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Pycharm()
l1 = Laptop()
l1.code(ide)
