numeros="0123456789"
NomeEq=["","","","",""]
PontosEq=[0,0,0,0]
GolosM=[0,0,0,0]
GolosS=[0,0,0,0]
NE=0
print("Introduza o resultado do jogo")
jogo=input()
while jogo=="":
    print("Introduza o resultado do jogo")
    jogo = input()
while jogo!="Fim":
    traco = jogo.find("-")
    if traco == -1:
        print("Nao tem traço")
    else:
        antes = jogo[0:traco]
        w = traco
        while jogo[w] != " " and w > 0:
            w = w - 1
        esp2 = jogo[traco + 1:len(jogo)].find(" ")
        res1 = jogo[w + 1:traco]
        res2 = jogo[traco + 1:esp2 + traco + 1]
        if numeros.find(res1) < 0 or numeros.find(res2) < 0:
            print("Resultado nao numerico")
        else:
            eq1 = jogo[0:w]
            NomeEq[NE] = eq1
            um = 0
            while NomeEq[um] != eq1:
                um = um + 1
            if um == NE:
                NE = NE + 1
            eq2 = jogo[esp2 + traco + 2:len(jogo)]
            NomeEq[NE] = eq2
            dois = 0
            while NomeEq[dois] != eq2:
                dois = dois + 1
            if dois == NE:
                NE = NE + 1
            if res1 > res2:
                PontosEq[um] = PontosEq[um] + 3
            elif res2 > res1:
                PontosEq[dois] = PontosEq[dois] + 3
            else:
                PontosEq[dois] = PontosEq[dois] + 1
                PontosEq[um] = PontosEq[um] + 1
            GolosM[um] = GolosM[um] + numeros.find(res1)
            GolosS[um] = GolosS[um] + numeros.find(res2)
            GolosM[dois] = GolosM[dois] + numeros.find(res2)
            GolosS[dois] = GolosS[dois] + numeros.find(res1)
    print("Introduza o resultado do jogo")
    jogo = input()
    while jogo == "":
        print("Introduza o resultado do jogo")
        jogo = input()

print("*******Tabela Final ********")
print("Equipa, Pontos, Golos marcados, Golos sofridos")
for i in range(NE):
    print(NomeEq[i], PontosEq[i],GolosM[i], GolosS[i])


for e1 in range(NE-1):
    for e2 in range(e1+1,NE):
        if PontosEq[e2]>PontosEq[e1] or PontosEq[e2]==PontosEq[e1] and GolosM[e2]-GolosS[e2]>GolosM[e1]-GolosS[e1] or PontosEq[e2]==PontosEq[e1] and GolosM[e2]-GolosS[e2]== GolosM[e1]-GolosS[e1] and GolosM[e2]> GolosM[e1] :
            Troca=NomeEq[e2]
            NomeEq[e2]=NomeEq[e1]
            NomeEq[e1]=Troca
            TrocaP = PontosEq[e2]
            PontosEq[e2] = PontosEq[e1]
            PontosEq[e1] = TrocaP
            TrocaG = GolosM[e2]
            GolosM[e2] = GolosM[e1]
            GolosM[e1] = TrocaG
            TrocaS = GolosS[e2]
            GolosS[e2] = GolosS[e1]
            GolosS[e1] = TrocaS

print("*******Tabela Final Ordenada ********")
print("Equipa, Pontos, Diferença de Golos ")
for i in range(NE):
    print(NomeEq[i], PontosEq[i],GolosM[i]- GolosS[i])