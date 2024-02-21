frase = input("Frase? ")
while frase == "":
    frase = input("Frase?")

alfa = "abcdefghijklmnopqrstuvwxyz"

for l in range(len(frase)):
    letra = frase[l]
    onde = alfa.find(letra)

    if onde != -1:
        print(letra)