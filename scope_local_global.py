
x=5000
def test():
    global y
    y=400
    x=5
    print("X=",x)
    d=globals()['x']
    print("global value of x=",d)

test()
print("bahar wala=",x)
print("local to global y=",y)