import turtle
turtle.bgcolor('black')
def drawshape(turtle,radius):
    turtle.circle(radius,extent=60)
    turtle.left(120)
    turtle.circle(radius,extent=60)

def drawflower():
    petal=turtle.Turtle()
    petal.color('pink')
    petal.speed(0)
    petal.pensize(4)
    no_of_petal=15
    radius=300
    for i in range(no_of_petal):
        drawshape(petal,radius)
        petal.left(360 / no_of_petal)

drawflower()
turtle.done()