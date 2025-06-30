f=open("apple.txt",'r')
print(f)
#print(f.read())
for data in f:
    print(data,end='')
f.close()

#f2=open("apple2.txt","w")
f2=open("apple2.txt","a")
print(f2)
f2.write(" ab dekho yeh bhi rahega")