start=int(input("enter start number"))
last=int(input("enter end number"))
if start<last:
    i=start
    while i<=last:
        if i % 2 == 0:
            print("even no=", i)
        else:
            print("Odd no=", i)
        i=i+1
else:
    i = start
    while i >= last:
        if i % 2 == 0:
            print("even no=", i)
        else:
            print("Odd no=", i)
        i = i - 1