# Inicialização de variáveis
ramo1 = 0
ramo2 = 0
ramo3 = 0

# Ler e validar k
print("Qual o valor de k?")
k = int(input())
while k < 0 or k > 10:
    print("Qual o valor de k?")
    k = int(input())

# Ciclo para k
while k != 0:
    maiorFx = 0
    maiorFx_X = 0

    print("************************")
    for x in range(-k, k + 1):
        if x <= 0:
            fx = abs(10 * x)
            ramo1 += 1
        elif x <= 4:
            fx = 1
            for i in range(x, 1, -1):
                fx = fx * i
            fx = fx / x
            ramo2 += 1
        else:
            fx = fx * 2
            ramo3 += 1
        if fx > maiorFx:
            maiorFx = fx
            maiorFx_X = x
        print("F(", x, ") = ", fx)
    print("************************")
    print("Mais elevado: F(", maiorFx_X, ") = ", maiorFx)
    print("************************")
    print("Qual o valor de k?")
    k = int(input())
    while k < 0 or k > 10:
        print("Qual o valor de k?")
        k = int(input())
print("Ramo Um: ", round((ramo1 / (ramo1 + ramo2 + ramo3)) * 100, 2), "%")
print("Ramo Dois: ", round((ramo2 / (ramo1 + ramo2 + ramo3)) * 100, 2), "%")
print("Ramo Três: ", round((ramo3 / (ramo1 + ramo2 + ramo3)) * 100, 2), "%")