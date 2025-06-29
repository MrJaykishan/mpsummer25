from turtle import *
t=Turtle()
l=['red','green','blue','orange','yellow']
t.pensize(10)
t.pu()
t.fd(200)
t.pd()
for i in range(5):
    t.circle(50)
    t.pencolor(l[i%5])
    t.pu()
    t.bk(200)
    t.pd()
done()