class A:
    def feature1(self):
        print('Feature A is working')
    def feature2(self):
        print('Feature 2 is working')


class B:
    def feature1(self):
        print('Feature B is working')
    def feature4(self):
        print('Feature 4 is working')


class C(B,A):
    def feature5(self):
        print('Feature 5 is working')
    def feature6(self):
        print('Feature 6 is working')
    def feature1(self):
        print('Feature C is working')    


c1 = C()
c1.feature1()

