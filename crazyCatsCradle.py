import turtle, random

t = turtle.Turtle()

i = 180
for j in range(i):
    myPenColor1 = (random.randint(0,100))/100
    myPenColor2 = (random.randint(0,100))/100
    myPenColor3 = (random.randint(0,100))/100
    t.pencolor(myPenColor1,myPenColor2,myPenColor3)
    t.forward(j*2)
    t.right(j)

input("Press Enter to continue...")