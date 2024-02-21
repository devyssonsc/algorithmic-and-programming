print("Qual o seu peso em kg?")
peso = int(input())

print("Qual a sua altura em centímetros?")
altura = int(input())

print("Qual a sua idade?")
idade = int(input())

print("Quantas vezes pratica exercício por semana?")
freqExercicio = int(input())

metab = 655 + (9.6 * peso) + (1.8 * altura) + (4.7 * idade)

kcal = 0

if freqExercicio >= 6:
    kcal = metab * 1.2
elif freqExercicio >= 4:
    kcal = metab * 1.55
elif freqExercicio >= 1:
    kcal = metab * 1.375
else:
    kcal = metab + 1.2

print("O nº de calorias que deve ingerir é", kcal,"calorias")