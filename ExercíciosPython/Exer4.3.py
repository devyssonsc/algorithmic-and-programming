Num=[0,0,0,0,0,0,0,0,0,0]
Nota=[[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0],[0,0,0], [0,0,0], [0,0,0]]
#[Inicializar número de alunos]
NA=0
# [Estabelecer ciclo para processar testes]
for T in range(3):
    #[Escrever cabeçalho]
    print("*** Teste", T+1," ***")
    #[Ler e validar número de aluno]
    print("Num? (0 para fim)")
    Num[NA]=int(input())
    while Num[NA]<0:
        print("Num? (0 para fim)")
        Num[NA] = int(input())
    # [Estabelecer ciclo para processar alunos]
    while Num[NA]!=0:
        #[Verificar se aluno já existe ou colocar novo aluno]
        K=0
        while Num[K] != Num[NA]:
            K = K + 1
        if K == NA:
            NA = NA + 1
            Nota[K][0] = -1
            Nota[K][1] = -1
            Nota[K][2] = -1
        # N70 [Ler e validar número de aluno]
        print("Nota?")
        Nota[K][T] = int(input())
        while Nota[K][T] < 0 or Nota[K][T] > 20:
            print("Nota?")
            Nota[K][T] = int(input())
        # [Ler e validar número do próximo aluno]
        print("Num? (0 para fim)")
        Num[NA] = int(input())
        while Num[NA] < 0:
            print("Num? (0 para fim)")
            Num[NA] = int(input())
    # [Estabelecer ciclo para processar alunos]
print("*** Notas de Alunos ***")
for A in range(NA):
    # [Calcular pior nota do Aluno e acumular soma notas]
    Soma = 0
    Min = 20
    for i in range(3):
        if Nota[A][i] < Min:
            Min = Nota[A][i]
        Soma = Soma + Nota[A][i]
        # [Calcular media de aluno]
    Media = (Soma - Min) / 2
    # [Escrever media de aluno]
    print(Num[A], ", nota ", Media)
print(" *** Médias de testes ***")
for T in range(3):
    # [Inicializar soma de notas de teste]
    soma = 0
    # [Inicializar número de alunos que fizeram teste]
    Quantos = 0
    # [Estabelecer ciclo para processar alunos]
    for i in range(NA):
        # [Atualizar contador de alunos e soma de notas de teste]
        if Nota[i][T] != -1:
            Quantos = Quantos + 1
            soma = soma + Nota[i][T]
        # [Calcular media de teste]
        if Quantos > 0:
            Media = soma / Quantos
        else:
            Media = 0
    # [Escrever media de teste]
    print("Média teste ", T, ": ", Media)