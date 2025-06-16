from math import sqrt
a=int(input("enter coffecient a"))
b=int(input("enter coffecient b"))
c=int(input("enter coffecient c"))
print("a=",a,"b=",b,"C=",c)
d=b*b-4*a*c
print("d=",d)
if d==0:
    print("roots are real and equal")
    x1=x2=-b/(2*a)
    print("X1=",x1,"X2=",x2)
elif d>0:
    print("roots are real and unequal")
    x1=(-b+sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("X1=", x1, "X2=", x2)
else:
    print("roots are imaginary")


