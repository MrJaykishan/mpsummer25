div=45/56
print(div)
print(format(div,'.4f'))
st="welcome to Python tutorial"
print(st)
print(len(st))
print(st.upper())
print(st.lower())
print(st.swapcase())
print(st.title())
print(st.capitalize())
print(st.endswith('l'))
print(st.count('to'))

st2="her name is tamanna amd tamanna is good girl"
rep="sonia"
#print(st2.replace('tamanna',rep,2))

search='t'
count=0
for i in st2:
    #print(i)
    if i==search:
        print("item found at loc=",count)
        break
    count=count+1
else:
    print("not found")

print(st2.index('t'))