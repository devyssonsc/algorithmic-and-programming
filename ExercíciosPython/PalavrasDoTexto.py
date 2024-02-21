#
texto = input("Texto: ")
while texto == "":
    texto = input("Texto: ")

#
novotexto = texto + " "

#
while novotexto != "":

    #
    esp = novotexto.find(" ")

    #
    palavra = novotexto[0:esp]

    #
    print(palavra)

    #
    novotexto = novotexto[esp+1: len(novotexto)]