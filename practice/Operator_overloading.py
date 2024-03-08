class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        self.m1 = self.m1 + other.m1
        self.m2 = self.m2 + other.m2
        s3 = Student(self.m1, self.m2)
        return s3

    def __gt__(self, other):

        return self.m1 + self.m2 > other.m1 + other.m2

    def __str__(self):
        return '{} {} '.format(self.m1, self.m2)


s1 = Student(20, 30)
s2 = Student(11, 12)

s3 = s1 + s2
print(s3.m1, s3.m2)

if (s1 > s2):
    print("s1 wins")
else:
    print("s2 wins")

print(s2)
