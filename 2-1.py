import random
n = random.randint(1,20)
print(n)
while True:
    a =int(input("input a number!"))
    if a == n:
        print('correct')
        break
    else:
        print('incorrect')
        
    

