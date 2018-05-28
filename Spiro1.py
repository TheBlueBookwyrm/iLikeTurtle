import turtle, random

t = turtle.Turtle()

i = 36
t.left(90)
for j in range(i):
    myPenColorR = random.random()
    myPenColorG = random.random()
    myPenColorB = random.random()

    t.pencolor(myPenColorR,myPenColorG,myPenColorB)
    t.forward(200)
    t.right(170)
    
input("Press Enter to continue...")