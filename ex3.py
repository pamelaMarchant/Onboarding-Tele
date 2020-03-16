a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

print("informe um numero: ")
y = int(input())

b = [x for x in a if x < y]
print(b)

print("\nLista")
for x in a:
    print(x)

print("\nRange")
for x in range(0, len(a)):
    print(x)
