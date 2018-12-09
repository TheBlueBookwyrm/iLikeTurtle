import turtle
import sys
from datetime import datetime


t = turtle.Turtle()

i = 200

print("\nProcess START: " + str(datetime.now()))

for x in range(i):
    t.forward(x)
    t.right(90)

print("Process END: " + str(datetime.now()))
    
if sys.version_info[0] >= 3:
    input("Press Enter to continue...")
else:
    raw_input("Press Enter to continue...")