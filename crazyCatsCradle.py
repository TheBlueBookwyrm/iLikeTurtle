import turtle, random

t = turtle.Turtle()

i = 180
for x in range(180):
    myPenColor1 = (random.randint(0,100))/100
    myPenColor2 = (random.randint(0,100))/100
    myPenColor3 = (random.randint(0,100))/100
    t.pencolor(myPenColor1,myPenColor2,myPenColor3)
    t.forward(x)
    t.right(x)

input("Press Enter to continue...")