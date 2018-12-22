import turtle
import random
import sys
from datetime import datetime

t = turtle.Turtle()

i = 36

#t.setx(-250)
#t.sety(-250)

print("\nProcess START: " + str(datetime.now()))

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

if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))

print("Please close graphics window to end program.")

turtle.mainloop()
