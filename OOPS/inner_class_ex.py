class Student:
    def __init__(self,name,roll,laptop):
        self.name= name
        self.roll =roll
        self.lap =laptop

    def show(self):
        print(self.name,self.roll ,self.lap.ram)


    class Laptop:
        def __init__(self,ram,company):
            self.ram =ram
            self.company =company    


lap = Student.Laptop('8gb','hp')
stu = Student('Samya','1',lap)
stu.show()