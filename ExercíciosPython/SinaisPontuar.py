F=[0,0,0,0,0]
#E10[Ler e validar texto]
print("Qual o texto?")
texto=input()
while texto=="":
    print("Qual o texto?")
    texto = input()
#E30 [Inicializar vetor de ocorrências]
for i in range(5):
    F[i]= 0
#E40[Inicializar número de sinais diferentes]
Qt=0
#E50 [Inicializar sonais]
Sinais=",?!;."
for i in range (len(texto)):
    car=texto[i]
    onde=Sinais.find(car)
    if onde!=-1:
        F[onde]=F[onde]+1
        if F[onde]==1:
            Qt=Qt+1
print("O texto tem",Qt," sinais de pontuação diferentes.")
print('*******')
Qt=0
for i in range(5):
    if F[i]>0:
        print(Sinais[i],"ocorre", F[i], "vezes")
        Qt=Qt+F[i]
print('*******')
print('Total de sinais de pontuação = ',Qt)
