import turtle
turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.penup()
a = 10
for i in range (30):
    turtle.stamp()
    a = a+3
    turtle.forward(a)
    turtle.right(24)
turtle.done()

