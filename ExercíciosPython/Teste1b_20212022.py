vit = 0
emp = 0
der = 0
pts = 0

print("Qual a primeira equipa? 'Nada' para terminar")
nome = input()
while nome == "":
    print("Qual a primeira equipa? 'Nada' para terminar")
    nome = input()

while nome != "Nada":

    saldoDeGol = 0

    print("Quantos jogos fez a equipa", nome, "?")
    jogos = int(input())
    while jogos <= 0:
        print("Quantos jogos fez a equipa", nome, "?")
        jogos = int(input())

    for j in range(jogos):

        print("********** Jogo", j + 1,"**********")

        print("Quantos gols marcou a equipa", nome,"?")
        golsFeitos = int(input())
        while golsFeitos < 0:
            print("Quantos gols marcou a equipa", nome, "?")
            golsFeitos = int(input())

        print("Quantos gols sofreu a equipa", nome, "?")
        golsContra = int(input())
        while golsFeitos < 0:
            print("Quantos gols sofreu a equipa", nome, "?")
            golsContra = int(input())

        saldoDeGol = saldoDeGol + (golsFeitos - golsContra)

        if golsFeitos > golsContra:
            vit = vit + 1
            pts = pts + 3
        elif golsFeitos == golsContra:
            emp = emp + 1
            pts = pts + 1
        else:
            der = der + 1



    print("********** Resumo", nome,"**********")
    print("Vitórias:", vit,"Empates:", emp,"Derrotas", der)
    print(pts,"pontos")
    print("Diferença de gols marcados e sofridos =", saldoDeGol)
    print("Gols Marcados", golsFeitos, "Gols Sofridos", golsContra)

    print("Qual a próxima equipa? 'Nada' para terminar")
    nome = input()
    while nome == "":
        print("Qual a próxima equipa? 'Nada' para terminar")
        nome = input()
    