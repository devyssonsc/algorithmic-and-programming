#T10[Inicializar contador de alunos com assiduidade]
ComAs = 0
#T20[Inicializar contador de alunos sem assiduidade]
SemAs = 0
#T30[Inicializar maior média de notas]
MediaMaxTodos = -1
#T40 [Inicializar acumulador de médias]
SomaMedias = 0
#T50 [Ler e validar o número de alunos da turma]
print("Quantos alunos tem a turma?")
Turma=int(input())
while Turma<=0:
    print("Quantos alunos tem a turma?")
    Turma = int(input())
    #T60 [Estabelecer ciclo para processar os elementos da turma]
for i in range(Turma):
    # T70 [Ler e validar nome de aluno]
    print("Nome do Aluno nº", i + 1)
    Nome = input()
    # T80 [Ler e validar percentagem de assiduidade do aluno]
    print("Qual a percentagem de assiduidade? (0-100)")
    Per = int(input())
    while Per < 0 or Per > 100:
        print("Qual a percentagem de assiduidade? (0-100)")
        Per = int(input())
    # T90 [Escrever mensagem se o aluno não tem assiduidade]
    if Per < 75:
        print(Nome, " não tem assiduidade, logo a nota é 0")
        # T100[Atualizar contador de alunos sem assiduidade]
        SemAs = SemAs + 1
    else:
        # T110 [Atualizar contador de alunos com assiduidade]
        ComAs = ComAs + 1
        # T120 [Inicializar três melhores notas do aluno]
        Max1 = 0
        Max2 = 0
        Max3 = 0
        # T130 [Ler e validar o número de testes do aluno]
        print("Quantos testes? (máximo 5)?")
        NumTestes = int(input())
        while NumTestes < 0 or NumTestes > 5:
            print("Quantos testes? (máximo 5)")
            NumTestes = int(input())
            # T140 [Estabelecer ciclo para processar teste dos alunos]
        for j in range(NumTestes):
            # T150 [Ler e validar nota de teste de aluno]
            print("Qual a nota do teste ", j + 1, "?")
            Nota = float(input())
            while Nota < 0 or Nota > 20:
                print("Qual a nota do teste ", j + 1, "?")
                Nota = float(input())
            # T160 [Actualizar 3 melhores notas do aluno]
            if Nota > Max1:
                Max3 = Max2
                Max2 = Max1
                Max1 = Nota
            elif Nota > Max2:
                Max3 = Max2
                Max2 = Nota
            elif Nota > Max3:
                Max3 = Nota
            # T170 [Calcular a media de teste do aluno]
        MediaTeste = (Max1 + Max2 + Max3) / 3
        # I175 [Atualizar soma de medias]
        SomaMedias = SomaMedias + MediaTeste
        # T180 [Calcular o valor correspondente à média do aluno]
        if MediaTeste >= 15:
            valor = 3
        elif MediaTeste >= 10:
            valor = 2
        elif MediaTeste >= 5:
            valor = 1
        else:
            valor = 0
        # T190 [Escrever média de testes do aluno e o valor correspondente]
        print(Nome, "tem média de ", MediaTeste, ", logo a nota é de ", valor, ".")
        # T200 [Atualizar melhor média de todos os alunos]
        if MediaTeste > MediaMaxTodos:
            MediaMaxTodos = MediaTeste
            NomeMaxTodos = Nome
# T210 [Escrever número de alunos com e sem assiduidade]
print("Há ", ComAs, " alunos com assiduidade e ", SemAs, " sem assiduidade.")
# T220 [Escrever nome e nota do aluno que teve a melhor média]
print("O ", NomeMaxTodos, " teve ", MediaMaxTodos, ", foi o melhor.")
# T230 [Escrever a média de médias da turma, apenas para os que tem assiduidade]
media = SomaMedias / Turma
print("A média da turma é ", round(media, 2))
# T240 [Terminar]