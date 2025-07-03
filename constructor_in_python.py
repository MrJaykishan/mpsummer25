class Student:
    def msg(self,book,college):
        self.book=book
        self.college=college
        print("this is example of oops")
        print(self.book,self.college)
    '''
    In Python, a constructor is a special method that is called automatically when an object is created from a class. Its main role is to initialize the
     object by setting up its attributes or state.
    '''
    # def __init__(self):
    #     print("I will without help of object")

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name,"age=",self.age)
        print("I will without help of object2")
s1=Student()
s=Student("ram",55)
s.msg('java','mp')
#s1=Student()
