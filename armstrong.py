n=int(input("enter any number"))
sum=0
orig=n
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=n//10

print("sum=",sum)
if sum==orig:
    print("arm strong")
else:
    print("not armstrong")