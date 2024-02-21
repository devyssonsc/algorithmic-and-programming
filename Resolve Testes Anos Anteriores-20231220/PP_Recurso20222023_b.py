Maius = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
Minus= "abcdefghijklmnopqrstuvwxyz"
Artigo = input("Qual a descrição do artigo? (Final para terminar)")
while len(Artigo) == 0:
    print("Não são aceites descrições vazias!")
    Artigo = input("Qual a descrição do artigo? (Final para terminar)")
MaiorStock=-1
MenorStock=9999999999
SomaStocks=0
QuantosArtigos=0
while Artigo!="Final":
    esp = Artigo.find(" ")
    Artigo = Artigo + " "
    NovoArtigo = ""
    while esp != -1:
        pal = Artigo[0:esp]
        prim = pal[0]
        if Maius.find(prim) == -1:
            if Minus.find(prim) >= 0:
                pal = Maius[Minus.find(prim)] + pal[1:len(pal)]
            else:
                pal = "*" + pal[1:len(pal)]
        for y in range(1, len(pal)):
            car = pal[y]
            if Minus.find(car) == -1:
                if Maius.find(car) >= 0:
                    pal = pal[0:y] + Minus[Maius.find(car)] + pal[y + 1:len(pal)]
                else:
                    pal = pal[0:y] + "#" + pal[y + 1:len(pal)]
        NovoArtigo = NovoArtigo + pal + "_"
        Artigo = Artigo[esp + 1:len(Artigo)]
        esp = Artigo.find(" ")
    NovoArtigo = NovoArtigo[0:len(Artigo) - 1]
    print("Qual stock? (>1)")
    stock = int(input())
    while stock < 1:
        print("Stock maior que 1, pf")
        print("Qual stock? (>1)")
        stock = int(input())
    print("***")
    print("Nova descrição: ", NovoArtigo, "Stock:", stock)
    print("***")
    QuantosArtigos=QuantosArtigos+1
    SomaStocks=SomaStocks+stock
    if MaiorStock<stock:
        MaiorStock=stock
        NomeMaiorStock=NovoArtigo
    if MenorStock > stock:
        MenorStock = stock
        NomeMenorStock = NovoArtigo
    Artigo = input("Qual a descrição do artigo? (Final para terminar)")
    while len(Artigo) == 0:
        print("Não são aceites descrições vazias!")
        Artigo = input("Qual a descrição do artigo? (Final para terminar)")
if QuantosArtigos==0:
    print("Nenhum Artigo processado")
else:
    Media=SomaStocks/QuantosArtigos
    print("***")
    print("Media =", Media)
    print("Maior stock = ", MaiorStock, "(",NomeMaiorStock,")")
    print("Menor stock = ", MenorStock, "(", NomeMenorStock, ")")