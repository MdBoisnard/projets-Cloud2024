from tkinter import font
from tkinter.font import nametofont
import turtle

LARGEUR, HAUTEUR = 640, 400

name = "Résurgence, rage de dents, urgence et excuses pour absence, SalutationS"


if __name__ == "__main__":
    turtle.setup(LARGEUR, HAUTEUR)
    turtle.speed("slow")
    ecart = 4
    for i in range(30):
        turtle.stamp()
        turtle.write('Hello! Résurgence, rage de dents, Aïe! urgence et excuses pour mon absence, SalutationS')
        turtle.left(60)
        turtle.up(); turtle.forward(ecart); turtle.down()
        ecart += 3
    turtle.exitonclick()




