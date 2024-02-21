print("Qual o número do atleta? (0 para terminar)?")
num=int(input())
while num<0:
    print("Qual o número do atleta? (0 para terminar)")
    num = int(input())
while num!=0:
    print("Quantos equipamentos quer comprar?")
    equipamentos = int(input())
    while equipamentos < 0:
        print("Quantos equipamentos quer comprar?")
        equipamentos = int(input())
    preco=0
    for i in range(equipamentos):
        print("Quer comprar (T)shirt, (C)alcão ou (M)eias?")
        tipo = input()
        while tipo != "T" and tipo != "C" and tipo != "M":
            print("Quer comprar (T)shirt, (C)alcão ou (M)eias?")
            tipo = input()
        if tipo=="T":
            preco=preco+20
        elif tipo=="C":
            preco = preco + 10
        else:
            preco = preco + 5
    print("O atleta ", num, " vai pagar", preco, "euros.")
    print("Qual o número do atleta? (0 para terminar)?")
    num = int(input())
    while num < 0:
        print("Qual o número do atleta? (0 para terminar)")
        num = int(input())
