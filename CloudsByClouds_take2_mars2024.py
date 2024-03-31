import turtle
import random


from matplotlib.patheffects import Stroke
from numpy import size

turtle.shape ("cloud")
turtle.color ("velvet")
turtle.bgcolor ("black")

t = turtle.Turtle()
s = turtle.Screen()

t.begin_fill ()
for i in range (0, 360):
    t.forward(1)
    t.left(1)
t.end_fill ()



##def setup():
   # size(1000, 1000)

 #   for c in range(50):
    #    center_x = random (200, 800)
   #     center_y = random (200, 800)

# draw Shadow
#noStroke()
#fill(15, 15, 15, 5)
#for i in range(30):
  #  turtle.circle (center_x, center_y, 150 - i*5)

    

#def semiCircle ():
 #   for i in range (0,20):
  #      t.forward(3)
   #     t.left(9)

#def turnRandom (maxTurn):
 #   rand = random.randint (0, maxTurn)
  #  t.left(180 + rand)


s.mainloop()



