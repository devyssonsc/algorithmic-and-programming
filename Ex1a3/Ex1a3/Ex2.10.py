print("Qual o seu sexo (F/M)")
sexo=input()
print ("Qual o peso?")
peso = int(input())
print ("Qual a altura? (m)")
altura = float(input())
IMC=peso/(altura*altura)
print ("IMC",IMC )
if sexo=="F":
 if IMC<19.1:
    print("Abaixo do peso")
 elif IMC<25.8:
    print("no peso normal")
 elif IMC < 27.3:
    print("marginalmente acima do peso")
 elif IMC < 32.3:
    print("Acima do peso ideal")
 else:
    print("Obeso")
else:
 if IMC < 20.7:
    print("Abaixo do peso")
 elif IMC < 26.4:
    print("no peso normal")
 elif IMC < 27.8:
    print("marginalmente acima do peso")
 elif IMC < 31.1:
    print("Acima do peso ideal")
 else:
    print("Obeso")