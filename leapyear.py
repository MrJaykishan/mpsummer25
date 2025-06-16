year=int(input("enter any year"))
print("year=",year)
if year%100==0:
    if year%400==0:
        print("year is leap")
    else:
        print("Not leap")
elif year%4==0:
    print("year is leap")
else:
    print("Not leap")