descArtigos = ["", "", "", "", "", "", "", "", "", ""]
stockArtigos = [0,0,0,0,0,0,0,0,0,0]

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

    ql = 0
    while descArtigos[ql] != novaDescrição and ql < contaArtigos:
        ql = ql + 1

    if ql < contaArtigos:
        stockArtigos[ql] = stockArtigos[ql] + stock

    else:
        descArtigos[contaArtigos] = novaDescrição
        stockArtigos[contaArtigos] = stock
        contaArtigos = contaArtigos + 1

    print("Nova descrição:", descArtigos[ql], "Stock:", stockArtigos[ql])
    print("***")

    if stockArtigos[ql] > stockMaiorStock:
        stockMaiorStock = stockArtigos[ql]
        descMaiorStock = descArtigos[ql]

    if stockArtigos[ql] < stockMenorStock:
        stockMenorStock = stockArtigos[ql]
        descMenorStock = descArtigos[ql]

    artigo = input("Qual a descrição do artigo? ")
    while len(artigo) == 0:
        print("Não são aceites descrições vazias!")
        artigo = input("Qual a descrição do artigo? ")


for i in range(contaArtigos):
    for j in range(contaArtigos-1):
        if stockArtigos[j] < stockArtigos[j+1]:
            stockArtigos[j], stockArtigos[j + 1] = stockArtigos[j + 1], stockArtigos[j]
            descArtigos[j], descArtigos[j + 1] = descArtigos[j + 1], descArtigos[j]

if contaArtigos > 0:
    print("***")
    for i in range(contaArtigos):
        print("Artigo:", descArtigos[i], "Stock:", stockArtigos[i])

    print("***")
    mediaStocks = somaStocks / contaArtigos
    print("Média:", mediaStocks)
    print("Maior Stock:", stockArtigos[0], "(", descArtigos[0], ")")
    print("Menor Stock:", stockArtigos[contaArtigos-1], "(", descArtigos[contaArtigos-1], ")")
else:
    print("Nenhum Artigo Processado")

