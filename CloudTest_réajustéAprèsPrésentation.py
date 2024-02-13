import turtle
import random

from random import randint
from numpy import angle


t = turtle.Turtle()
s = turtle.Screen()
#turtle.hideturtle()


s.bgcolor("black")
#t.pencolor("grey")
t.speed(500)

Xaléa = random.randint(0, 150)
Yaléa = random.randint(0, 150)

#def positionInitiale(Xaléa, Yaléa) :
for i in range(10):
    t.penup()
    t.goto(Xaléa, Yaléa)
    t.pendown()


#def Clouds(diamètre, angle) :
    for i in range(250):
        t.circle(50)
        t.left(1)
        t.circle(50)
        t.left(1)
        t.pencolor("green")
    
    for i in range(250):
        t.circle(150)
        t.right(1)
        t.circle(150)
        t.right(1)
        t.pencolor("grey")
    
    for i in range(250):
        t.circle(100)
        t.left(1)
        t.circle(100)
        t.left(1)
        t.pencolor("orange")











s.mainloop()



