class Computer:

    mouse = 1

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

    @classmethod
    def cls_example(cls):
        print(cls.mouse)


com1 = Computer("i5", 16)
com2 = Computer("i3", 8)
com1.config()
com2.config()

Computer.cls_example()
