f=open("apple2.txt","r")
f1=open("apple3.txt",'w')
for data in f:
    print(data)
    f1.write(data)
f1.close()
f.close()


