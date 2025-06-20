from numpy import *
arr1=array([1,2,3,4,5])
print("arr1",arr1,"Address of arr1=",id(arr1))
arr2=arr1 # aliasing method
print("arr2",arr2,"Address of arr2=",id(arr2))
print("After changing the value of arr2")
arr2[0]=5678
print("arr2",arr2,"Address of arr2=",id(arr2))
print("arr1",arr1,"Address of arr1=",id(arr1))
print("Anothe copy view method")
arr3=array([1,2,30,4,50])
print("arr3",arr3,"Address of arr3=",id(arr3))
arr4=arr3.view() #shallow copy
print("arr4",arr4,"Address of arr4=",id(arr4))
print("After changing the value of arr4")
arr4[0]=1000
print("arr4",arr4,"Address of arr4=",id(arr4))
print("arr3",arr3,"Address of arr3=",id(arr3))

print("Anothe copy  method")
arr5=array([133,23,30,4,50])
print("arr5",arr5,"Address of arr5=",id(arr5))
arr6=arr5.copy() #deep copy
print("arr6",arr6,"Address of arr6=",id(arr6))
print("After changing the value of arr6")
arr6[0]=888
print("arr6",arr6,"Address of arr6=",id(arr6))
print("arr5",arr5,"Address of arr5=",id(arr5))