import turtle
import random
import sys
from datetime import datetime

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
t.pencolor("white")
t.hideturtle()

c = turtle.Turtle()
c.pencolor("white")
c.hideturtle()

numDots = random.randint(10, 250)

limitX, limitY = c.screen.screensize()
c.penup()
c.goto(limitX, limitY)

print("\nProcess START: " + str(datetime.now()))

for i in range(numDots):
    tx, ty = t.position()
    t.forward(1)
    t.penup()
    angle = random.randint(1, 359)
    t.right(angle)
    skip = random.randint(1, 100)
    t.forward(skip)
    if tx < -200 or tx > 200 or ty < -200 or ty > 200:
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        t.goto(x, y)
    t.pendown()
    c.clear()
    c.write(str(i+1) + " of " + str(numDots))


if t.isvisible():
    t.hideturtle()

print("Process END: " + str(datetime.now()))

print("Please close graphics window to end program.")

turtle.mainloop()
