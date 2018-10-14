import turtle
import random
import sys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
t.pencolor("white")
t.hideturtle()

numDots = random.randint(10, 250)

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

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")