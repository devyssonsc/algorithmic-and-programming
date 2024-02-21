comecaTerminaLetra = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
freqComecaTerminaLetra = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contaComecaTerminaLetra = 0
contaDifComecaTerminaLetra = 0

comecaVogal = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
freqComecaVogal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contaComecaVogal = 0
contaDifComecaVogal = 0

vogais = "aeiou"

texto = input("Texto: ")
while texto == "":
    texto = input("Texto: ")

novoTexto = texto + " "

letra = input("Letra: ")
while letra == "":
    letra = input("Letra: ")

contaPalavras = 0

onde = novoTexto.find(" ")

while onde != -1:
    palavra = novoTexto[0:onde]

    tam = len(palavra)

    firstLetter = palavra[0]
    lastLetter = palavra[tam-1]

    if vogais.find(firstLetter) != -1:
        ql = 0
        while comecaVogal[ql] != palavra and ql < contaDifComecaVogal:
            ql += 1

        if ql < contaDifComecaVogal:
            freqComecaVogal[ql] += 1
        else:
            comecaVogal[ql] = palavra
            freqComecaVogal[ql] = 1
            contaDifComecaVogal += 1

        contaComecaVogal += 1

    if firstLetter == letra and lastLetter == letra:
        ql = 0
        while comecaTerminaLetra[ql] != palavra and ql < contaDifComecaTerminaLetra:
            ql += 1

        if ql < contaDifComecaTerminaLetra:
            freqComecaTerminaLetra[ql] += 1
        else:
            comecaTerminaLetra[ql] = palavra
            freqComecaTerminaLetra[ql] = 1
            contaDifComecaTerminaLetra += 1

        contaComecaTerminaLetra += 1

    contaPalavras += 1

    novoTexto = novoTexto[onde+1 : len(novoTexto)]

    onde = novoTexto.find(" ")

print("Há", contaPalavras, "palavras no texto.")
print("Começadas por", letra, "e terminadas por", letra, "há", contaComecaTerminaLetra, "palavras")

difComecaTerminaLetra = ""
for i in range(contaDifComecaTerminaLetra):
    if i == 0:
        difComecaTerminaLetra = comecaTerminaLetra[i]
    else:
        difComecaTerminaLetra += "," + comecaTerminaLetra[i]

print("Começadas por", letra, "e terminadas por", letra, "há", contaDifComecaTerminaLetra, "palavras diferentes (", difComecaTerminaLetra, ")")



print("Há", contaComecaVogal, "palavras começadas por vogais")

difComecaVogal = ""
for i in range(contaDifComecaVogal):
    if i == 0:
        difComecaVogal = comecaVogal[i]
    else:
        difComecaVogal += "," + comecaVogal[i]

print("Há", contaDifComecaVogal, "palavras diferentes começadas por vogais (", difComecaVogal, ")")