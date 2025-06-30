f=open("nest.gif","br")
f1=open("best.gif",'bw')
for data in f:
    print(data)
    f1.write(data)
f1.close()
f.close()