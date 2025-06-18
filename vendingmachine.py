n=int(input("How many toffe u want"))
stock=15
i=1
while i<=n:
    if i<=stock:
        print("Please collect toffe=",i)
    else:
        print("Out of Stock")
        break
    i=i+1
else:
    print("thank u please visit again")