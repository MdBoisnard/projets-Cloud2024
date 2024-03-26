import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.screensize(800, 300)

t.pensize(1)

##ajuster la vitesse execution (0, 10, 6, 3, 1)
t.speed(10)


Xalea = random.randint(0, 100)
Yalea = random.randint(0, 100)

##def PositionInitiale(Xalea, Yalea)
for i in range(4):
    t.penup()
    t.goto(Xalea, Yalea)
    t.pendown()
    
##def Clouds(diametre, angle, couleur)
    for i in range(250):
        t.circle(25)
        t.left(1)
        t.circle(50)
        t.left(1)
        t.pencolor("red")
        

    for i in range(250):
        t.circle(100)
        t.right(1)
        t.circle(125)
        t.right(1)
        t.pencolor("grey")
        

    for i in range(250):
        t.circle(75)
        t.left(1)
        t.circle(100)
        t.left(1)
        t.pencolor("orange")
        


s.mainloop()






