for n in range(3,101):
    i=2
    while i<=n-1:
        if n%i==0:
            
            break
        i=i+1
    else:
        print("Prime no=",n)