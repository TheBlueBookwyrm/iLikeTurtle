import turtle, random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(0,0,0)
t.pencolor("white")
t.hideturtle()

limitX, limitY = t.screen.screensize()

numDots = random.randint(10,100)

#blue, aliceblue, white, lightyellow, yellow, orange, red
#1,1,1,3,7,12,75
colorList = []
colorList.append("blue")
colorList.append("aliceblue")
colorList.append("white")
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
    angle = random.randint(1,359)
    t.right(angle)
    skip = random.randint(1,100)
    t.forward(skip)
    if tx < (-1 * limitX) or tx > limitX or ty < (-1 * limitY) or ty > limitY:
        x = random.randint(-1 * limitX,limitX)
        y = random.randint(-1 * limitY,limitY)
        t.goto(x,y)
    t.pendown()    
    j = random.randint(0,99) 
    t.pencolor(colorList[j])

input("Press Enter to continue...")
