ps=0
max = 0
nomemax= "???"
kg=0
print ("Introduza o nome da primeira pessoa: (fim para terminar)")
nome=input()
while nome!="fim":
    ps=ps+1
    paga=0
    print ("Quantas frutas diferentes comprou o ", nome)
    qts=int(input())
    while qts<=0:
        print("Quantas frutas diferentes comprou o ", nome)
        qts = int(input())
    for i in range(qts):
        print("Qual a fruta que comprou(B)ananas, (K)iwis, (L)aranjas, (P)essegos: ")
        fruta=input()
        while fruta!="B" and fruta!="K" and fruta!="L" and fruta!="P":
            print("Qual a fruta que comprou(B)ananas, (K)iwis, (L)aranjas, (P)essegos: ")
            fruta = input()
        print("Peso: ")
        peso= float(input())
        while peso <= 0:
            print("Peso")
            peso = float(input())
        kg=kg+peso
        if fruta=="B":
            paga=paga+peso*0.99
        elif fruta=="K":
            paga=paga+peso*2.2
        elif fruta=="L":
            paga=paga+peso*1.25
        else:
            paga=paga+peso*1.75
    print("O ", nome, " paga ", paga, "euros ")
    if paga > max:
        max = paga
        nomemax = nome
    print("Introduza o nome da proxima pessoa: (fim para terminar)")
    nome = input()
print("**********")
print("O ", nomemax, " foi quem pagou mais = ", max, " euros ")
media = kg / ps
print("Foram processadas ", ps, " pessoas que compraram em media ", media, " kg")