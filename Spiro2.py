import turtle
import random
import sys

t = turtle.Turtle()

i = 72

#t.setx(-250)
#t.sety(-250)

for x in range(4):
    for j in range(i):
        myPenColorR = random.random()
        myPenColorG = random.random()
        myPenColorB = random.random()

        t.pencolor(myPenColorR, myPenColorG, myPenColorB)
        t.forward(250)
        t.right(85)
    t.left(90)

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")