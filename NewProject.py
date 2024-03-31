import turtle
import random


from matplotlib.pyplot import draw
from turtle import done

#maud est notre tortue
maud = turtle.Turtle()

maud.color("blue")
maud.fillcolor("yellow")
maud.begin_fill()

while True:
    maud.forward(280)
    maud.left(250)
    if abs(maud.pos()) < 1:
        break

maud.end_fill()


maud.screen.mainloop()


done()




