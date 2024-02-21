#Contatenar
Texto1="bom dia"
Texto2="a todos"
Texto=Texto1+" "+Texto2
print(Texto)
#Tamanho
tamanho=len(Texto)
print("tamanho =", tamanho)
#Encontrar
p1="dia"
p2="Pedro"
Onde1=Texto.find(p1)
Onde2=Texto.find(p2)
if Onde1==-1:
    print("Nao encontrei", p1)
else:
    print("Encontrei", p1, "na posicao",Onde1+1)
if Onde2==-1:
    print("Nao encontrei", p2)
else:
    print("Encontrei", p2, "na posicao",Onde2+1)

#Extrair
letraqual=4
UmaLetra=Texto[letraqual]
print(letraqual , "letra de ",Texto,"=",UmaLetra)
Dupleto=Texto[letraqual:letraqual+2]
print("dupleto com inicio em ",letraqual , "=",Dupleto)
AteAoFim=Texto[letraqual:len(Texto)]
print("Desde",letraqual , "ate ao fim =",AteAoFim)