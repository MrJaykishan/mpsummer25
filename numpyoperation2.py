from numpy import *
a=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a)
print(a.shape)
print(a.ndim)

b=array([
    [1,2,3],
    [4,5,6],
    [7,8,9],

])

#print(a+b)
#for matrix multiplication
print(a@b)
print(dot(a,b))
