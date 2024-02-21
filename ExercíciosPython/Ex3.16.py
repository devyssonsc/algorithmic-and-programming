maiorminiteste = 0
somaminiteste = 0
notamelhoraluno = 0
nomemelhoraluno = ""
somanotasfinais = 0
qtdalunos = 0
qtdrep = 0
qtdoral = 0
qtdap = 0

print("Número? (0 para terminar)")
num = int(input())
while num < 0:
    print("Número? (0 para terminar)")
    num = int(input())

while num != 0:
    maiorminiteste = 0
    somaminiteste = 0
    print("Nome?")
    nome = input()
    while nome == "":
        print("Nome?")
        nome = input()

    print("Quantos testes fez o aluno", num, "-", nome, "? (1 a 5)")
    qtdtestes = int(input())
    while qtdtestes <= 0 or qtdtestes > 5:
        print("Quantos testes fez o aluno", num, "-", nome, "? (1 a 5)")
        qtdtestes = int(input())

    for i in range(qtdtestes):

        print("Qual a nota do aluno", num, "-", nome, " no teste", i + 1, "? (0 a 20)")
        nota = int(input())
        while nota <= 0 or nota > 20:
            print("Qual a nota do aluno", num, "-", nome, " no teste", i + 1, "? (0 a 20)")
            nota = int(input())

        somaminiteste = somaminiteste + nota

        if nota > maiorminiteste:
            maiorminiteste = nota

    if qtdtestes > 1:
        notafinal = 0.5 * maiorminiteste + 0.5 * ((somaminiteste - maiorminiteste) / (qtdtestes - 1))
    else:
        notafinal = 0.5 * somaminiteste

    if notafinal > notamelhoraluno:
        notamelhoraluno = notafinal
        nomemelhoraluno = nome
    somanotasfinais = somanotasfinais + notafinal
    qtdalunos = qtdalunos + 1
    print("***********************************")
    print(num, "-", nome, "teve nota final", notafinal)
    if notafinal <= 8:
        resultado = "Reprovado"
        qtdrep = qtdrep + 1
    elif notafinal <= 12:
        resultado = "Oral"
        qtdoral = qtdoral + 1
    else:
        resultado = "Aprovado"
        qtdap = qtdap + 1
    print(resultado)
    print("***********************************")
    print("Número?")
    num = int(input())
    while num < 0:
        print("Número?")
        num = int(input())
if qtdalunos == 0:
    print("Ninguém Processado")
else:
    print("O aluno", nomemelhoraluno, "teve a melhor nota = ", notamelhoraluno)
    print("Média de notas = ", somanotasfinais/qtdalunos)
    print((qtdap / qtdalunos) * 100, "Aprovados", (qtdoral / qtdalunos) * 100, "Oral", (qtdrep / qtdalunos) * 100, "Reprovados")
