sexo = input(("Sexo? (F, M ou Fim para terminar)"))
e1=0
e2=0
e3=0
e4=0
e5=0
while sexo != "F" and sexo != "M" and sexo != "Fim":
    sexo = input(("Sexo? (F, M ou Fim para terminar)"))
Contar=0
SomaIMC=0
while sexo != "Fim":
    peso = float(input("Introduza o seu peso: "))
    while peso < 40 or peso > 150:
        peso = float(input("Introduza o seu peso: "))
    altura = int(input("Introduza a sua altura em cm: "))
    while altura < 100 or altura > 250:
        altura = int(input("Introduza a sua altura em cm: "))
    IMC = peso / altura ** 2 * 10000
    print("IMC =", round(IMC,2))
    Contar=Contar+1
    SomaIMC=SomaIMC+IMC
    if sexo == "F":
        if IMC < 19.1:
            print("Abaixo do peso")
            e1=e1+1
        elif IMC < 25.8:
            print("No peso normal")
            e2=e2+1
        elif IMC < 27.3:
            print("Marginalmente acima do peso")
            e3=e3+1
        elif IMC < 32.3:
            print("Acima do peso ideal")
            e4=e4+1
        else:
            print("Obeso")
            e5=e5+1
    else:
        if IMC < 20.7:
            print("Abaixo do peso")
            e1=e1+1
        elif IMC < 26.4:
            print("No peso normal")
            e2=e2+1
        elif IMC < 27:
            print("Marginalmente acima do peso")
            e3=e3+1
        elif IMC < 31.1:
            print("Acima do peso ideal")
            e4=e4+1
        else:
            print("Obeso")
            e5=e5+1
    sexo = input(("Sexo? (F, M ou Fim para terminar)"))
    while sexo != "F" and sexo != "M" and sexo != "Fim":
        sexo = input(("Sexo? (F, M ou Fim para terminar)"))
if Contar == 0:
 print("Ninguem")
else:
 media=SomaIMC/Contar
 print("n*****")
 print("media=",round(media,2))
 print("Ha", e5, "obesos")
 print("Ha", e4, "acima do peso")
 print("Ha", e3, "Marginalmente acima do peso")
 print("ha", e2, "normal")
 print("Ha", e1, "abaixo do peso")