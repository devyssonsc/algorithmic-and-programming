vogais = "aeiou"

frase = input("Frase('Fim' para terminar): ")
while frase == "":
    frase = input("Frase('Fim' para terminar): ")

contaPalavrasTotal = 0

while frase != "Fim":

    novaFrase = frase + " "

    palavras = ["","","","","","","","","","","","","","","","","","","","",]

    qtVogais = 0

    onde = novaFrase.find(" ")

    contaPalavras = 0

    while onde != -1:

        palavra = novaFrase[0:onde]

        for i in range(len(palavra)):
            if vogais.find(palavra[i]) != -1:
                qtVogais += 1

        palavras[contaPalavras] = palavra

        contaPalavras += 1

        novaFrase = novaFrase[onde + 1 : len(novaFrase)]

        onde = novaFrase.find(" ")


    contaPalavrasTotal += contaPalavras

    listaPalavras = ""
    for j in range(contaPalavras):
        if palavras[j] != "":
            listaPalavras += str(j+1) + "-" + palavras[j] + " "

    print(listaPalavras)
    print("Em", frase, "há", qtVogais, "vogais")

    frase = input("Frase('Fim' para terminar): ")
    while frase == "":
        frase = input("Frase('Fim' para terminar): ")

print("Encontrei", contaPalavrasTotal, "palavras.")