'''
pass an agument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keyword variable length argumnent
'''
def person(name,age,status='single'):
    print("name=",name)
    age=age+10
    print("age=",age)
    print("status=",status)

#1. positional argument
person("abcd",89)
#person(55,"xyz")

#2. keyword argument
person(age=66,name="ashwani",status="married")

#3 default argument