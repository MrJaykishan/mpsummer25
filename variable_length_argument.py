#4. variable length argument (*)
def add(a,b,c):
    print(a+b+c)

add(2,3,9)

def autoadd(a,*b):
    #print(a,type(a))
    #print(b,type(b))
    sum=a
    for i in b:
        sum=sum+i
    return sum
print(autoadd(1,4))

def autoadd1(*b):
    sum1=0
    for i in b:
        sum1=sum1+i
    return sum1
print(autoadd1(1,2,3,3,5,9))