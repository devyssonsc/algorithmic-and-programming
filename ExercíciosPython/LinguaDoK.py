vogais = "aeiou"
sozinhasFreq = [0,0,0,0,0]

acompVogais = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
acompFreq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

frase = input("Qual a frase?('Terminar' para fim) ")
while frase == "":
    frase = input("Qual a frase?('Terminar' para fim) ")

print("***")

contaPalavras = 0

tamAcompVogais = 0

while frase != "Terminar":

    novaFrase = frase + " "

    onde = novaFrase.find(" ")

    fraseK = ""

    while onde >= 0:

        palavra = " " + novaFrase[0:onde] + " "

        palavraK = ""

        conjuntoVogais = ""

        for i in range(len(palavra)):
            if vogais.find(palavra[i]) != -1:

                if vogais.find(palavra[i-1]) != -1:

                    conjuntoVogais += palavra[i]
                    palavraK = palavraK + conjuntoVogais + "K" + conjuntoVogais

                    ql = 0
                    while acompVogais[ql] != conjuntoVogais and ql < tamAcompVogais:
                        ql = ql + 1

                    if ql < tamAcompVogais:
                        acompFreq[ql] += 1
                    else:
                        acompVogais[tamAcompVogais] = conjuntoVogais
                        acompFreq[ql] = 1
                        tamAcompVogais = tamAcompVogais + 1

                else:
                    conjuntoVogais = palavra[i]
                    if vogais.find(palavra[i+1]) == -1:
                        palavraK = palavraK + conjuntoVogais + "K" + conjuntoVogais
                        sozinhasFreq[vogais.find(palavra[i])] += 1

            else:
                conjuntoVogais = ""
                palavraK = palavraK + palavra[i]

        palavraK = palavraK[1: len(palavraK)]

        print(palavraK)

        fraseK = fraseK + palavraK

        contaPalavras += 1

        novaFrase = novaFrase[onde + 1 : len(novaFrase)]

        onde = novaFrase.find(" ")

    print("***")
    print(fraseK[0 : len(fraseK)-2])

    frase = input("Qual a frase?('Terminar' para fim) ")
    while frase == "":
        frase = input("Qual a frase?('Terminar' para fim) ")


if contaPalavras > 0:
    print("Vogais sozinhas")
    print("***")
    for s in range(5):
        if sozinhasFreq[s] > 0:
            print(vogais[s], "aparece", sozinhasFreq[s], "vezes")

    print("***")
    print("Vogais acompanhadas")
    print("***")
    for a in range(tamAcompVogais):
        if acompFreq[a] > 0:
            print(acompVogais[a], "aparece", acompFreq[a], "vezes")
else:
    print("Nenhuma frase processada!")