print("Quanto mede o primeiro lado?")
lado1 = int(input())

print("Quanto mede o segundo lado?")
lado2 = int(input())

print("Quanto mede o terceiro lado?")
lado3 = int(input())

#Qual o maior lado(A)?
a = 0
if lado1 > lado2:
    if lado1 > lado3:
        a = lado1
        b = lado2
        c = lado3
    else:
        a = lado3
        b = lado1
        c = lado2
else:
    if lado2 > lado3:
        a = lado2
        b = lado1
        c = lado3
    else:
        a = lado3
        b = lado1
        c = lado2

if a >= b + c:
    print("Não se forma nenhum triângulo.")
elif a**2 == b**2 + c**2:
    print("Forma-se um triângulo retângulo")
elif a ** 2 > b ** 2 + c ** 2:
    print("Forma-se um triângulo obtuso")
elif a**2 < b**2 + c**2:
    print("Forma-se um triângulo agudo")

