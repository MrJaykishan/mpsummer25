from turtle import *
t=Turtle() # creating object of turtle class
t.speed(1) #help('turtle.speed')
t.shape('turtle')
t.hideturtle()
t.pu()
t.goto(50,50)
t.pd()
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.pd()
def sq():
    t.fd(100)
    t.left(90)
for i in range(4):
    sq()
done()