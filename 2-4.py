import turtle,time,random
a = turtle.Turtle()
turtle.shape('turtle')
b=random.randint(30,90)
c=1
while True:
    a.forward(200)
    a.left(b)
    c=c+1
    b=random.randint(30,90)
    a.right(b)
    if c>50:
        break
    
    
