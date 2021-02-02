import random
n = random.randint(1,10)
b = 10
s = 1
t = 0
print(s,b)

while True:
    if t == 5:
        print('gameover')
        break
    a =int(input("input a number!"))
    
    if a == n:
        print('correct')
        t = t + 1
        print(t,'time')
        break
    elif a>=b or a<=s:
        print('error')
        t = t + 1
    elif a>n:
        b=a
        print(s,b)
        t = t + 1
    elif a<n:
        s=a
        print(s,b)
        t = t + 1
        