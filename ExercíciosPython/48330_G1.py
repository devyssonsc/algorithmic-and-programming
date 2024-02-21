alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

artigo = input("Qual a descrição do artigo? ")
while len(artigo)==0:
    print("Não são aceites descrições vazias!")
    artigo = input("Qual a descrição do artigo? ")

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

print("Nova descrição:", novaDescrição)