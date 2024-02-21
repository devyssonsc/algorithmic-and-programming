print("Qual o seu nome?")
Nome=input()
print("Qual o número de horas extras? ")
Extra=int(input())
print("E quantas vezes faltou?")
Faltas=int(input())
Formula=Extra-2/3*Faltas
if Formula>40:
 Bonus=50
elif Formula>30:
 Bonus=25
elif Formula>20:
 Bonus=12.5
elif Formula > 10:
 Bonus = 7.5
else:
 Bonus = 5
print("Bónus = ", Bonus," euros")