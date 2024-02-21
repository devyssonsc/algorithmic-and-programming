alunos = ["","","","","","","","","","","","","","","","","","","",""]
mediasAlunos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mediasPorExtenso = ["","","","","","","","","","","","","","","","","","","",""]

qtAlunos = int(input("Quantos alunos tem na turma? "))
while qtAlunos == "" or qtAlunos <= 0:
    qtAlunos = int(input("Quantos alunos tem na turma? "))

for aluno in range(qtAlunos):
    print("Nome do Aluno n°", aluno + 1, "? ")
    nomeAluno = input()
    while nomeAluno == "":
        print("Nome do Aluno n°", aluno + 1, "? ")
        nomeAluno = input()

    notasAluno = [0,0,0,0]
    qtTestesFeitos = 0

    for teste in range(4):
        if teste <= qtTestesFeitos:
            print("Nota do", nomeAluno, "no ", teste + 1, "teste? (-1 para terminar) ")
            notaTeste = int(input())
            while notaTeste > 20 or notaTeste < -1:
                print("Nota do", nomeAluno, "no ", teste + 1, "teste? (-1 para terminar) ")
                notaTeste = int(input())
            if notaTeste != -1:
                notasAluno[teste] = notaTeste
                qtTestesFeitos += 1

    for i in range(4):
        for j in range(4):
            if notasAluno[i] > notasAluno[j]:
                notasAluno[i], notasAluno[j] = notasAluno[j], notasAluno[i]


    media = 0
    if qtTestesFeitos > 0:
        media += notasAluno[0] * 0.5

        somaResto = 0
        for nota in range(1, qtTestesFeitos):
            somaResto += notasAluno[nota]

        media += (somaResto / (qtTestesFeitos-1)) * 0.5

    alunos[aluno] = nomeAluno
    mediasAlunos[aluno] = media

for i in range(qtAlunos):
    porExtenso = ""
    aux = str(mediasAlunos[i])
    for j in range(len(aux)):
        if aux[j] == "1":
            porExtenso += "um "
        elif aux[j] == "2":
            porExtenso += "dois "
        elif aux[j] == "3":
            porExtenso += "três "
        elif aux[j] == "4":
            porExtenso += "quatro "
        elif aux[j] == "5":
            porExtenso += "cinco "
        elif aux[j] == "6":
            porExtenso += "seis "
        elif aux[j] == "7":
            porExtenso += "sete "
        elif aux[j] == "8":
            porExtenso += "oito "
        elif aux[j] == "9":
            porExtenso += "nove "
        elif aux[j] == "0":
            porExtenso += "zero "
        elif aux[j] == ".":
            porExtenso += "ponto "
    mediasPorExtenso[i] = porExtenso


somaTodos = 0
for s in range(qtAlunos):
    somaTodos += mediasAlunos[s]

mediaTodos = somaTodos / qtAlunos

print("***************")
print("Média de todos:", mediaTodos)
print("***************")

for a in range(qtAlunos):
    for b in range(qtAlunos):
        if mediasAlunos[a] > mediasAlunos[b]:
            mediasAlunos[a], mediasAlunos[b] = mediasAlunos[b], mediasAlunos[a]
            alunos[a], alunos[b] = alunos[b], alunos[a]
            mediasPorExtenso[a], mediasPorExtenso[b] = mediasPorExtenso[b], mediasPorExtenso[a]

for aluno in range(qtAlunos):
    print("***", alunos[aluno], "***")
    print("Média:", mediasAlunos[aluno], "(", mediasPorExtenso[aluno], ")")
    print("Diferença média turma: ", (mediasAlunos[aluno] - mediaTodos))