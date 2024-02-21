#artigos = ["", "", "", "", "", "", "", "", "", "",]
#stockArtigos = [0,0,0,0,0,0,0,0,0,0]

alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

artigo = input("Qual a descrição do artigo? ('Final' para terminar) ")
while len(artigo)==0:
    print("Não são aceites descrições vazias!")
    artigo = input("Qual a descrição do artigo? ('Final' para terminar) ")

contaArtigos = 0
somaStocks = 0
stockMaiorStock = 0
descMaiorStock = ""
stockMenorStock = 9999999999999
descMenorStock = ""


while artigo != "Final":

    stock = int(input("Qual stock? (>1)"))
    while stock <= 1:
        print("Stock maior que 1, pf")
        stock = int(input("Qual stock? (>1)"))

    somaStocks = somaStocks + stock

    print("***")

    primeiraLetra = 0
    novaDescrição = ""

    for c in range(len(artigo)):
        if alfa.find(artigo[c]) != -1:
            if primeiraLetra == 0:
                novaDescrição = novaDescrição + artigo[c].upper()
                primeiraLetra = 1
            else:
                novaDescrição = novaDescrição + artigo[c].lower()

        elif artigo[c] == " ":
            novaDescrição = novaDescrição + "_"
            primeiraLetra = 0

        else:
            if primeiraLetra == 0:
                novaDescrição = novaDescrição + "*"
                primeiraLetra = 1
            else:
                novaDescrição = novaDescrição + "#"

    contaArtigos = contaArtigos + 1

    print("Nova descrição:", novaDescrição, "Stock:", stock)
    print("***")

    if stock > stockMaiorStock:
        stockMaiorStock = stock
        descMaiorStock = novaDescrição

    if stock < stockMenorStock:
        stockMenorStock = stock
        descMenorStock = novaDescrição

    artigo = input("Qual a descrição do artigo? ")
    while len(artigo) == 0:
        print("Não são aceites descrições vazias!")
        artigo = input("Qual a descrição do artigo? ")

if contaArtigos > 0:
    mediaStocks = somaStocks / contaArtigos
    print("Média:", mediaStocks)
    print("Maior Stock:", stockMaiorStock, "(", descMaiorStock, ")")
    print("Menor Stock:", stockMenorStock, "(", descMenorStock, ")")
else:
    print("Nenhum Artigo Processado")