qtdMaiorEquipe = 0
valorMaisCara = 0
catA = 0
catB = 0
catC = 0

print("Qual o nome da equipe?")
nome = input()
while nome == "":
    print("Qual o nome da equipe?")
    nome = input()

while nome != "Final":
    print("Quantos elementos tem a equipe", nome, "?")
    qtdElementos = int(input())
    while qtdElementos <= 0:
        print("Quantos elementostem a equipe", nome, "?")
        qtdElementos = int(input())

    for x in range(qtdElementos):

        print("Qual a categoria do ", x+1,"º elemento da equipe", nome, "?")
        cat = input()
        while cat != "A" and cat != "B" and cat != "C":
            print("Qual a categoria do ", x+1, "º elemento da equipe", nome, "?")
            cat = input()

        if cat == "A":
            catA += 1
        elif cat == "B":
            catB += 1
        else:
            catC += 1

    print("Quantas medalhas gravadas pretende?")
    qtdMedalhas = int(input())
    while qtdMedalhas < 0 or qtdMedalhas > qtdElementos:
        print("Quantas medalhas gravadas pretende?")
        qtdMedalhas = int(input())

    valorPago = qtdElementos * 15 + qtdMedalhas * 10

    print("A equipe", nome, "paga", valorPago, "euros")

    if qtdElementos > qtdMaiorEquipe:
        qtdMaiorEquipe = qtdElementos
        nomeMaiorEquipe = nome

    if valorPago > valorMaisCara:
        valorMaisCara = valorPago
        nomeMaisCara = nome

    print("Qual o nome da equipe?")
    nome = input()
    while nome == "":
        print("Qual o nome da equipe?")
        nome = input()

print("A equipe", nomeMaiorEquipe, "é a maior equipe em número (", qtdMaiorEquipe, "atletas)")
print("A equipe", nomeMaisCara, "é a equipe que mais paga (", valorMaisCara, "euros)")
print(round((catA/(catA + catB + catC)) * 100, 1), "% categoria A")
print(round((catB/(catA + catB + catC)) * 100, 1), "% categoria B")
print(round((catC/(catA + catB + catC)) * 100, 1), "% categoria C")