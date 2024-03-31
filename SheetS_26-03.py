import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.screensize(800, 300)

t.pensize(1)

def random_walk(t):
    for _ in range(200):
        t.speed(random.choice("800,1200"))
        t.color(random.choice("r,g,b"))
        t.forward(random.choice("1, 50"))


#def Clouds(diamètre, angle) :
    for i in range(250):
        t.circle(50)
        t.left(1)
        t.circle(50)
        t.left(1)  
    
    for i in range(250):
        t.circle(125)
        t.right(1)
        t.circle(125)
        t.right(1)


    for i in range(250):
        t.circle(100)
        t.left(1)
        t.circle(100)
        t.left(1)



s.mainloop()