import turtle
import random
import sys

if len(sys.argv) < 3:
    print("Please call this program as follows:")
    print("    stars.py lolim hilim")
    print("where lolim and hilim are integers and lolim <= hilim")
    exit()

try:
    dotsLower = int(sys.argv[1])
except ValueError:
    print("The value for the LOWER limit of the number of stars must be an integer")
    exit()

try:
    dotsUpper = int(sys.argv[2])
except ValueError:
    print("The value for the UPPER limit of the number of stars must be an integer")
    exit()

if dotsUpper >= dotsLower:
    numDots = random.randint(dotsLower, dotsUpper)
    print(str(numDots) + " stars will be plotted")
else:
    print("The value for the upper limit of stars must be larger than the value for the lower limit.") 
    exit()

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0, 0, 0)
t.pencolor("white")
t.hideturtle()

limitX, limitY = t.screen.screensize()

# blue, aliceblue, white, lightyellow, yellow, orange, red
# 1,1,1,3,7,12,75
colorList = ["blue", "aliceblue", "white"]
for s in range(3):
    colorList.append("lightyellow")
for s in range(7):
    colorList.append("yellow")
for s in range(12):
    colorList.append("orange")
for s in range(75):
    colorList.append("orangered1")

for i in range(numDots):
    tx, ty = t.position()
    t.forward(1)
    t.penup()
    angle = random.randint(1, 359)
    t.right(angle)
    skip = random.randint(1, 100)
    t.forward(skip)
    if tx < (-1 * limitX) or tx > limitX or ty < (-1 * limitY) or ty > limitY:
        x = random.randint(-1 * limitX, limitX)
        y = random.randint(-1 * limitY, limitY)
        t.goto(x, y)
    t.pendown()    
    j = random.randint(0, 99)
    t.pencolor(colorList[j])

input("Press Enter to continue...")
