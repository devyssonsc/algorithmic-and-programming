pals = ["","","","","","","","","","","","","","","","","","","","",]
freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

texto = input("Texto: ")
while texto == "":
    texto = input("Texto: ")

novoTexto = texto + " "

conta = 0

onde = novoTexto.find(" ")

while onde > -1:

    palavra = novoTexto[0:onde]

    pals[conta] = palavra
    freq[conta] = 1

    ql = 0
    while pals[ql] != palavra and ql <= conta:
        ql += 1

    if ql < conta:
        freq[ql] += 1
    else:
        conta += 1

    novoTexto = novoTexto[onde+1 : len(novoTexto)]

    onde = novoTexto.find(" ")

if conta > 0:
    for i in range(conta):
        print(pals[i], "ocorre", freq[i], "vezes")