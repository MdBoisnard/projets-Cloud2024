
from turtle import Turtle
from turtle import done
from random import random

maud = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    circle = int(random() * 40)
    maud.right(angle)
    maud.fd(steps)


maud.screen.mainloop()
maud.screen.bgcolor("orange")




done()



