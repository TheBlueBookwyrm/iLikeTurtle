import turtle
import random
import sys

t = turtle.Turtle()

i = 36
t.left(90)
for j in range(i):
    myPenColorR = random.random()
    myPenColorG = random.random()
    myPenColorB = random.random()

    t.pencolor(myPenColorR, myPenColorG, myPenColorB)
    t.forward(200)
    t.right(170)
    
if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")