class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class B:

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("feature 3")


class C(B, A):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feature4(self):
        print("feature 4")


c1 = C()
