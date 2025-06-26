from turtle import *
t=Turtle() # creating object of turtle class
t.speed(1) #help('turtle.speed')
t.shape('turtle')
t.circle(100)
t.circle(-50)
t.right(90)
t.fd(50)
t.pencolor('blue')
for i in range(24):
    t.right(15)
    t.fd(50)
    t.bk(50)
# t.undo()
# t.clear()
t.reset()

done()