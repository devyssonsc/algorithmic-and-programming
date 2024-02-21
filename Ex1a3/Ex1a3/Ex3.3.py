vezes = 0
soma = 0
print("Qual o nome do comprador? (não vazio, fim para fim)")
Nome = input()
while Nome == "":
    print("Qual o nome do comprador? (não vazio, fim para fim)")
    Nome = input()
while Nome != "fim":
    print("Qual a cilindrada do motor? (>450cc)")
    Cilindrada = int(input())
    while Cilindrada<450:
        print("Qual a cilindrada do motor? (>450cc)")
        Cilindrada = int(input())
    if Cilindrada <= 1250:
        IA = 3.74*Cilindrada-2417.56
    else:
        IA = 8.86*Cilindrada-8813.22
    print("O Sr. ", Nome, "paga IA = ", round(IA,2)," euros.")
    print("Qual o nome do comprador? (não vazio, fim para fim)")
    vezes = vezes+1
    soma = soma+IA
    Nome = input()
    while Nome == "":
        print("Qual o nome do comprador? (não vazio, fim para fim)")
        Nome = input()
if vezes == 0:
    print("Nenhum carro processado")
else:
    media = soma / vezes
    print('Total IA ', round(soma, 2), 'e media IA', round(media, 2))