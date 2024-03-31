import turtle
import random

from random import randint
from matplotlib import colors
from numpy import angle
from tkinter import colorchooser


t = turtle.Turtle()
s = turtle.Screen()
turtle.hideturtle()


s.bgcolor("black")
s.screensize(800, 300)


t.speed(800)
t.pensize(1)

Xaléa = random.randint(-100, 100)
Yaléa = random.randint(-100, 100)

def random_walk(t):
    t.speed(800)
    t.pensize(1)
    for _ in range(200):
        t.speed(random.choice("800,1200"))
        t.color(random.choice("r,g,b"))
        t.forward(random.choice("Xaléa, Yaléa"))





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
        t.pencolor("red")
        
    
    for i in range(250):
        t.circle(125)
        t.right(1)
        t.circle(125)
        t.right(1)
        t.pencolor("grey")
    
    for i in range(250):
        t.circle(100)
        t.left(1)
        t.circle(100)
        t.left(1)
        t.pencolor("orange")



s.mainloop()



