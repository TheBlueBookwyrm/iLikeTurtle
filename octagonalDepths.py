import turtle
import sys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)

t.pencolor("white")
i = 200
for x in range(i):
    t.pencolor(x/i, x/i, x/i)
    t.forward(x)
    t.right(45)

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")