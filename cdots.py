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
# 400,300

# print(limitX, limitY)

t.penup()
#t.setx(0)
#t.sety(0)

mypensize = 1

e = float(limitX)
f = float(limitY)

t.setx(-limitX)
t.sety(limitY)
t.pendown()

for j in range (limitX):
    for i in range (limitY):
        t.pencolor(i/e, j/f, 1)
        t.forward(1)
    t.penup()
    t.setx(-limitX)
    t.sety(limitY - j)
    t.pendown()

print("Process END: " + str(datetime.now()))

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")