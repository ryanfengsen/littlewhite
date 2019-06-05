import turtle
def drawLine(size,color):
    for i in range(size):
        turtle.color(color)
        turtle.fd(i)
        turtle.seth(90 *(i+1))

drawLine(100,"blue")
