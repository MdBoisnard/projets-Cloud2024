import turtle
import random

# Configurations de base
colors = ["red", "green", "blue", "orange"]
sizes = [50, 75, 100, 125]
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Fonction pour dessiner un cercle
def draw_circle(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

# Dessiner les cercles
for _ in range(250):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.choice(sizes)
    color = random.choice(colors)
    draw_circle(x, y, size, color)

# Afficher le dessin
turtle.mainloop()