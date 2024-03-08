class Demo:
    def __init__(self,name,age):
        self.age =age
        self.name = name
        

    def println(self):
       print('name:',self.name,' age:' , self.age )


    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False
    
    @classmethod
    def clsMethod(cls):
        print('This is a class method')
    

    @staticmethod
    def staticMtd():
        print('this is static method')
obj = Demo('Samya',30)
obj1 = Demo('Sameer',30)
obj.println()
obj1.println()
Demo.clsMethod()
obj1.staticMtd()



