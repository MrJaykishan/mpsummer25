def add(a,b):
    c=a+b
    return c
f=add(56,56)
print(f)
print("Sum of a and b=",f)
print(add(5,6))

def calci(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

add,sub,mul,div=calci(10,5)
print(add,sub,mul,div)