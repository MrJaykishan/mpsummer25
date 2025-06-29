from turtle import *
t=Turtle()
t.shape('turtle')
t.color('goldenrod','black')
s=2
t.speed(1)

for i in range(3):
    #t.setpos(30,30)
    t.stamp()
    t.pu()
    t.setpos(30, 30)
    t.fd(50)

    t.pd()


# l=['red','green','blue','orange','yellow']
#
# for i in range(1,100):
#     t.fd(10%i)
#     t.left(5)
#     t.pencolor(l[i%5])
#     t.pensize(i%50)


done()