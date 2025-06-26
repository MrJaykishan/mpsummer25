from functools import *
l=[1,3,555,33,66,22,856,4533,444]

even_no_list=list(filter(lambda n:n%2==0,l))
print(even_no_list)

odd_no_list=list(filter(lambda n:n%2!=0,l))
print(odd_no_list)

output=list(map(lambda n:n+5,even_no_list))
print(output)

data=reduce(lambda a,b:a+b,output)
print(data)