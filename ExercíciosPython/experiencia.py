print("Valor de k")
k = int(input())

while k != 0:
    if k <= 4:
        fx = 1
        for i in range(k, 0, -1):
            fx = fx * i
        fx = fx / k
    else:
        fx = fx * 2

    print("F(", k, ")=", fx)

    print("Valor de k")
    k = int(input())