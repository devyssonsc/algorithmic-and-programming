print ("Qual o seu peso em kg?")
peso = int(input())
print ("Qual a sua altura em centímetros?")
altura = float(input())
print ("Qual a sua idade? ")
idade=int(input())
print ("Quantas vezes pratica exercício por semana?")
vezes=int(input())
Meta=655 + 9.6 * peso + 1.8 * altura + 4.7 * idade
if vezes==0:
 Cals=Meta*1.2
elif vezes<=3:
 Cals = Meta * 1.375
elif vezes<=5:
 Cals = Meta * 1.55
else:
 Cals = Meta * 1.725
print ("O nº de calorias que deve ingerir é ", Cals,"calorias")