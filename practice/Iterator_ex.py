class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        val = self.num
        if self.num <= 10:
            self.num += 1
            return val
        else:
            raise StopIteration


value = TopTen()

for i in value:
    print(i)
