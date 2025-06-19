from numpy import *
'''
there are six different ways to create an array
1. array
2. linspace
3. logspace
4. arange
5. zeros
6. ones
'''
a=array([1,2,3,4,5,6])
print(a)
print(a.dtype)
# linspace
# b=linspace(1,15,10)
# print(b)
#
# c=logspace(1,15)
# print(c)

d=arange(1,10,2)
print(d)

e=zeros(100,int)
print(e)

f=ones(10)
print(f)
print(f.dtype)