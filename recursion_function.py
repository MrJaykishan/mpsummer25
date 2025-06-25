import sys
print(sys.getrecursionlimit())
limit=sys.setrecursionlimit(2000)
print(limit)
def msg():
    print("hi")
    msg()


msg()