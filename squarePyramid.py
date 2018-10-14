import turtle
import sys

t = turtle.Turtle()

i = 200
for x in range(i):
    t.forward(x)
    t.right(90)
    
if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")