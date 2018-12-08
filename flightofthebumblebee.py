import turtle
import random
import sys

t = turtle.Turtle()

i = 50
t.left(90)
for j in range(i):
    myPenColorR = random.random()
    myPenColorG = random.random()
    myPenColorB = random.random()

    t.pencolor(myPenColorR, myPenColorG, myPenColorB)
    t.forward(i)
    turn = random.randint(1, 359)
    t.right(turn)
    
if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")