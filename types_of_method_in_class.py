'''
1.instance method- which accepts self as an argument

'''
class Student:
    school_name="Mp Polytechnic" # class variable
    def get_marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        print("m1=",self.m1,"m2=",self.m2,"m3=",self.m3)

    def get_total_marks(self):
        return self.m1+self.m2+self.m3
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    @staticmethod
    def msg():
        print("this is static method and it will run without object")

Student.msg()
print(Student.get_school_name())
s=Student()
s.get_marks(10,20,30)
print(s.get_total_marks())
