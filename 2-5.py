import turtle,time
tu = turtle.Turtle()
tr = turtle.Turtle()
while True:
    s = int(input('how many side?(4-10)'))
    if s <= 10 and s>=4:
        break
    else:
        print('error')
side_length = 100
an = 360 / s
for a in range(s):
    for i in range(s):
        tu.forward(side_length)
        tr.forward(side_length)
        time.sleep(1)
        tu.left(an)
        tr.right(an)
    side_length=side_length-10
    
turtle.done()
    