
from tkinter.font import Font
from turtle import*

maud = Turtle()

import random

#Création triangle initial

maud.forward(200)
maud.left(120)
maud.forward(200)
maud.left(120)
maud.forward(200)
maud.left(120)


#Déplacement No draw
forward(200)
up()
forward(50)
down()
forward(200)

maud.pendown()
circle(120)


Xaléa = random.randint(-450, 450)
Yaléa = random.randint(-450, 450)

def PositionInitiale(Xaléa, Yaléa) :
    for _ in range(0, 3) :
        maud.circle(40)
        maud.penup()
        maud.goto(Xaléa, Yaléa)
        maud.pendown()
        maud.circle(60)
        maud.penup()

#ajouterUnTexte
maud.pendown()
maud.write("MyBE2024")
maud.penup()
maud.goto(Xaléa, Yaléa)
maud.pendown()
maud.circle(60)




done()

