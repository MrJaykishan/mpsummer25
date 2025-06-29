from turtle import *
t=Turtle()
sc=Screen()
sc.listen()
def moveFd():
    t.fd(100)
def moveBk():
    t.bk(100)
def moveLeft():
    t.left(90)
def moveRight():
    t.right(90)
#sc.onkey(moveFd, 'Up')
sc.onkey(moveFd,'B')
sc.onkey(moveBk,'Down')
sc.onkey(moveLeft,'Left')
sc.onkey(moveRight,'Right')
done()