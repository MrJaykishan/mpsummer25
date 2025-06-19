from array import *
a=array('f',[1,2,3,4,5.0,6,7])
print(a)

for i in a:
    print(i)

print(a.typecode)
print(len(a))
print(a.buffer_info())
print("Add=",sum(a))