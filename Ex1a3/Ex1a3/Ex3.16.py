conta=0
total=0
Ap=0
Oral=0
Rep=0
print("Numero? (0 para terminar)")
num=int(input())
while num<0:
    print("Numero? (0 para terminar)")
    num = int(input())
maiorNota=0
while num != 0:
    conta=conta+1
    print("Nome? ")
    nome = input()
    while nome == "":
        print("Nome? ")
        nome = input()
    print("Quantos testes fez o aluno ", num,"-",nome,"? (1 a 5)")
    n=int(input())
    while n<0 or n>5:
        print("Quantos testes fez o aluno ", num, "-", nome, "? (1 a 5)")
        n = int(input())
    soma=0
    max=0
    for i in range(n):
        print("Qual a nota do aluno", num, "-", nome, "no teste ", i + 1, "? (0 a 20)")
        nota = int(input())
        while nota < 0 or nota > 20:
            print("Qual a nota do aluno", num, "-", nome, "no teste ", i + 1, "? (0 a 20)")
            nota = int(input())
        soma = soma + nota
        if max < nota:
            max = nota
    if n > 1:
       media = (soma - max) / (n - 1)
    else:
       media = 0
    final = 0.5 * max + 0.5 * media
    if maiorNota < final:
        maiorNome = nome
        maiorNota = final
    total = total + final
    print("*******************************************")
    print(num, "-", nome, "teve nota final", final, "= 50%*", max, "+50%*", media)
    if final < 8:
        print("Reprovado")
        Rep = Rep + 1
    elif final < 12:
        print("Oral")
        Oral = Oral + 1
    else:
        print("Aprovado")
        Ap = Ap + 1
    print("*******************************************")
    print("Numero? (0 para terminar)")
    num = int(input())
    while num < 0:
       print("Numero? (0 para terminar)")
       num = int(input())
if conta == 0:
    print("Ninguem processado")
else:
    print("O aluno", maiorNome, "teve a melhor nota =", maiorNota)
    print("Média de notas =", total / conta)
    print(Ap / conta * 100, "% Aprovados", Oral / conta * 100, "% oral", Rep / conta * 100, "% Reprovados")