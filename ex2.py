print ("informe um numero: ")
n1 = int(input())

print ("informe um outro numero: ")
n2 = int(input())

div = n1 % n2
resto = n1 % 2
multi = n1 % 4

if resto == 0:
    print ("numero par")
else:
    print("numero impar")

if multi == 0:
    print ("numero multiplo de 4")

if div == 0:
    print ("dividiu certo")
else:
    print ("dividiu errado")
