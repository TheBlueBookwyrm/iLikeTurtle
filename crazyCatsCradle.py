import turtle
import random
import sys

t = turtle.Turtle()

i = 180
for j in range(i):
    myPenColor1 = (random.randint(0, 100))/100
    myPenColor2 = (random.randint(0, 100))/100
    myPenColor3 = (random.randint(0, 100))/100
    t.pencolor(myPenColor1, myPenColor2, myPenColor3)
    t.forward(j*2)
    t.right(j)

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")
