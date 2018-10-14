import turtle
import sys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
#s.bgcolor(1, 1, 1)

t.pencolor("white")
i = 200
for x in range(i):
    f = float(i)
#    print(str(f), str(x), str(x/f))
    t.pencolor(x/f, x/f, x/f)
    t.forward(x)
    t.right(45)

if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")