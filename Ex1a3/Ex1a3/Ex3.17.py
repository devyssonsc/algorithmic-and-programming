#Inicializar o maior numero de artigos
Maior=0
#Inicializar o maior volume em preco
MaiorValor=0
#Incializar Contadores totais de tipo
TC=0
TE=0
TB=0
#Incializar acumulador totais por tipo
VTc=0
VTb=0
VTe=0
#Estabelecer ciclo para processar os 5 Amigos
for i in range(5):
    # U10 [Ler e validar o nome do amigo]
    print("Nome?")
    Nome = input()
    while Nome == "":
        print("Nome?")
        Nome = input()
    # U20 [Incializar número de artigos do Amigo]
    Conta = 0
    # U30 [Incializar Contadores de tipo]
    C = 0
    E = 0
    B = 0
    # U40 [Incializar acumulador por tipo]
    Vc = 0
    Vb = 0
    Ve = 0
    # U50 [Ler e validar o tipo de primeiro artigo]
    print("Tipo comida (C), bebidas (B), extras (E) ou (F)im")
    Tipo = input()
    while Tipo != "C" and Tipo != "B" and Tipo != "E" and Tipo != "F":
        print("Tipo comida (C), bebidas (B), extras (E) ou (F)im")
        Tipo = input()
    # U60 [Estabelecer ciclo para processar artigo do Amigo]
    while Tipo != "F":
        # U70[Ler validar preço do artigo]
        print("Preço do artigo?")
        Preco = int(input())
        while Preco < 0:
            print("Preço do artigo?")
            Preco = int(input())
        # U80[Acumular artigo]
        if Tipo == "C":
            C = C + 1
            Vc = Vc + Preco
        elif Tipo == "B":
            B = B + 1
            Vb = Vb + Preco
        else:
            E = E + 1
            Ve = Ve + Preco
        # U90[Incrementar número de artigos do Amigo]
        Conta = Conta + 1
        # U100[Ler e validar o tipo de próximo artigo]
        print("Tipo comida (C), bebidas (B), extras (E) ou (F)im")
        Tipo = input()
        while Tipo != "C" and Tipo != "B" and Tipo != "E" and Tipo != "F":
            print("Tipo comida (C), bebidas (B), extras (E) ou (F)im")
            Tipo = input()
    # Atualizar Quem e quanto foi o Amigo que mais artigos levou
    if Maior < Conta:
        Maior = Conta
        MaiorNome = Nome
    # [Atualizar Quem e quanto foi o Amigo que mais valor de artigos levou]
    if MaiorValor < Vb + Ve + Vc:
        MaiorValor = Vb + Ve + Vc
        MaiorValorNome = Nome
    # Acumular totais por tipo e valor
    TB = TB + B
    VTb = VTb + Vb
    TC = TC + C
    VTc = VTc + Vc
    TE = TE + E
    VTe = VTe + Ve
    # U110 [Escrever número de artigos que o Amigo levou]
    print("O ", Nome, "levou", Conta, "artigos ")
# U120 [Escrever os artigos que o Amigo levou por tipo: número e total]
    if B > 0:
        print(B, " bebida ", Vb, "euros ")
    if C > 0:
        print(C, " comida ", Vc, "euros ")
    if E > 0:
        print(E, " extras ", Ve, "euros ")
    # U130 [Escrever total de preco dos artigos do Amigo]
    print("Total ", Vb + Ve + Vc, "euros")
# [Escrever quem foi o Amigo que levou mais artigos]
print("O ", MaiorNome, "foi quem levou mais artigos: ", Maior, ".")
# Escrever quem foi o Amigo que levou mais em valor]
print("O", MaiorValorNome, "foi quem levou mais em valor: ", MaiorValor, " euros. ")
# Escrever total de artigos por tipo, assim como o respetivo valor]
print(TB, "bebida", TC, "comida e ", TE, "extra, respetivamente ", VTb, ",", VTc, "e", VTe, " euros")
# U140 [Terminar]
# Exit []
