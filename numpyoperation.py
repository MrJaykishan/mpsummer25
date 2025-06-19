from numpy import *

a=array([1,2,3,4,5,6])
print(a)
x=a.reshape(3,2)
print(x)
print(x.flatten())
print(a.size)
print(a.shape)
print(a.ndim)

print(a+5)

b=array([7,7,7,7,7,7])
print(a+b)
print(b[1:5])
