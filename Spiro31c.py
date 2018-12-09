import turtle
import random
import sys

t = turtle.Turtle()

i = 36

#t.setx(-250)
#t.sety(-250)

for x in range(8):
    myPenColorR = 0
    myPenColorG = 0
    fx = float(x)
    myPenColorB = float(fx) / (fx + 1)

    t.pencolor(myPenColorR, myPenColorG, myPenColorB)

    for j in range(i):

        t.forward(250)
        t.right(170)
    t.left(45)

t.hideturtle()

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")