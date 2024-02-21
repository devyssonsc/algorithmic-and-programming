print("Qual o seu nome?")
nome = input()

print("Qual o número de horas extras?")
horasExtras = int(input())

print("E quantas vezes faltou?")
faltas = int(input())

horasTotais = horasExtras - 2 / 3 * faltas

if horasTotais > 40:
    print("Bónus = 50€")
elif horasTotais >= 30:
    print("Bónus = 25€")
elif horasTotais >= 20:
    print("Bónus = 12.5€")
elif horasTotais >= 10:
    print("Bónus = 7.5€")
else:
    print("Bónus = 5€")