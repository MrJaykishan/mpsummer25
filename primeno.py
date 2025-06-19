n=6
i=2
while i <=n-1:
    if n % i == 0:
        print("not Prime=", n)
        break
    i = i + 1
else:
    print("Prime no=", n)