print("Qual o seu sexo? (F ou M)")
sexo = input()

print("Qual o seu peso?")
peso = int(input())

print("Qual a sua altura em metros?")
altura = float(input())

imc = peso / ( altura**2 )
print("IMC = ", round(imc,1))


if sexo == "F":
    if imc < 19.1:
        print("Está abaixo do peso")
    elif imc <= 25.8:
        print("Está no peso normal")
    elif imc <= 27.3:
        print("Está marginalmente acima do peso")
    elif imc <= 32.3:
        print("Está acima do peso ideal")
    else:
        print("Está obesa")
else:
    if imc < 20.7:
        print("Está abaixo do peso")
    elif imc <= 26.4:
        print("Está no peso normal")
    elif imc <= 27.8:
        print("Está marginalmente acima do peso")
    elif imc <= 31.1:
        print("Está acima do peso ideal")
    else:
        print("Está obeso")