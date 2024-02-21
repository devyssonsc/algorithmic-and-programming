print("Qual o nome do aluno (Fim para terminar)")
Nome=input()
while Nome!="Fim":
    print("Qual o ano de nascimento?")
    ano = int(input())
    while ano < 1996 or ano > 2004:
        print("Qual o ano de nascimento?")
        ano = int(input())
    print("Qual o numero de treinos por semana?")
    nvezes = int(input())
    while nvezes < 1 or nvezes > 5:
        print("Qual o numero de treinos por semana?")
        nvezes = int(input())
    if ano <= 1998:
        preco = nvezes * 30
        cat ="expert"
    elif ano <= 2001:
        preco = nvezes * 25
        cat = "intermédios"
    else:
        preco = nvezes * 20
        cat = "minis"
    print("O(A)",Nome," vai pagar ",preco, "euros por mês (",cat,").")
    print("Qual o nome do proximo aluno (Fim para terminar)")
    Nome = input()