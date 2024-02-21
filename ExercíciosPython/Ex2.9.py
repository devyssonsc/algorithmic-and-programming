print("Qual o nome do comprador?")
comprador = input()

print("Qual é a marca do veículo?")
marca = input()

print("Qual é o modelo do veículo?")
modelo = input()

print("QUal é a cilindrada do motor?")
cc = int(input())

if cc <= 1250:
    ia = 3.74 * cc - 2417.56
else:
    ia = 8.86 * cc - 8813.22

print("IA = ", round(ia,2))