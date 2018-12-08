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
t.setx(-limitX)
t.sety(limitY)
t.pendown()

for i in range (limitX * 2):
    t.forward(1)

t.right(90)

for j in range (limitY * 2):
    t.forward(1)

t.right(90)

for i in range (limitX * 2):
    t.forward(1)

t.right(90)

for j in range (limitY * 2):
    t.forward(1)



print("Process END: " + str(datetime.now()))

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")