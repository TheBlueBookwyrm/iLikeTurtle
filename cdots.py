import turtle
import sys
from datetime import datetime


print("\nProcess START: " + str(datetime.now()))

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
t.pencolor("white")
t.hideturtle()

limitX, limitY = t.screen.screensize()

t.penup()
t.setx(-limitX)
t.sety(limitY)
t.pendown()

mypensize = 1

#e = float(limitY)
#f = float(limitX)

myLim = 24

e = float(myLim)

for j in range (myLim):
    for i in range (myLim):
        for g in range (myLim):

#        print(str(i) + " " + str(j))

            t.pencolor(i/e, j/e, g/e)
            t.forward(1)
#        t.penup()
#        t.forward(1)
#        t.pendown()
        t.penup()
        t.setx(-limitX + (j * myLim))
#        t.sety(limitY - (i + (j * myLim)))
        t.sety(limitY - i)
#        print(limitY, i)
        t.pendown()

print("Process END: " + str(datetime.now()))

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")