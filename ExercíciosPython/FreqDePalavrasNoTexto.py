#
pal = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",]

#
freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#
texto = input("Texto: ")
while texto == "":
    texto = input("Texto: ")

#
novoTexto = texto + " "

#
contaPalavras = 0

#
onde = novoTexto.find(" ")

#
while onde >= 0:

    #
    palavra = novoTexto[0:onde]

    #
    pal[contaPalavras] = palavra
    freq[contaPalavras] = 1
    qt = 0

    while pal[qt] != palavra:
        qt = qt + 1


    if qt<contaPalavras:
        freq[qt] = freq[qt] + 1
    else:
        contaPalavras = contaPalavras + 1

    #
    novoTexto = novoTexto[onde + 1 : len(novoTexto)]

    #
    onde = novoTexto.find(" ")

#
for p in range(contaPalavras):

    #
    if freq[p] > 0:
        print(pal[p], "ocorre", freq[p], "vezes")