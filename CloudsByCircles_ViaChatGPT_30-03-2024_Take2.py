import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.screensize(800, 300)

t.pensize(1)

##ajuster la vitesse execution (0, 10, 6, 3, 1)
t.speed(0)

Xalea = random.randint(-300, 300)
Yalea = random.randint(-200, 200)

for i in range(4):
    t.penup()
    t.goto(Xalea, Yalea)
    t.pendown()

    if i == 0:
        diametre = 25
        couleur = "red"
    elif i == 1:
        diametre = 50
        couleur = "grey"
    elif i == 2:
        diametre = 75
        couleur = "orange"
    else:
        diametre = 100
        couleur = "blue"

    for _ in range(250):
        t.pencolor(couleur)
        t.circle(diametre)
        t.left(1)
        diametre += 25

s.mainloop()


## Crédits
## Cet algorithme a été développé en collaboration avec un assistant virtuel pour créer un effet visuel de nuages avec des cercles de différentes tailles et couleurs.
## L'assistant virtuel a contribué en fournissant des suggestions algorithmiques basées sur nos interactions. Cette collaboration a permis de créer un résultat esthétique et visuellement intéressant.
##Pour plus d'informations sur la collaboration, vous pouvez consulter [cette conversation]()https://chat.openai.com/c/49132029-5129-4bea-bc52-728211a17622.