import turtle
tu=turtle.Turtle()
def square(l,s):
    for i in range(s):
        tu.forward(l)
        tu.left(90)
l=10
s = int(input("input side"))
for a in range(s):
    square(l,s)
    l=l+10