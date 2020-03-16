import random

cont = 1
x = random.randint(0, 10)
z = ""
while z != "exit":
    print("advinhe um numero entre 1 e 10: ")
    cont = cont+1
    z = input()
    if z != "exit":
        y = int(z)
        if y < x:
            print("baixo")
        if y > x:
            print("alto")
        if y == x:
            print("igual")
            print(cont)
