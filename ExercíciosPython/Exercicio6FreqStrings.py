F=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#E10[Ler e validar texto]
print("Qual o texto?")
texto=input()
while texto=="":
    print("Qual o texto?")
    texto = input()
#E20 [Guardar o texto inicial]
TextoInicial=texto
texto=texto+" "
#E30 [Inicializar vetor de ocorrências]
for i in range(26):
    F[i]= 0
#E40[Inicializar número de palavras]
Qt=0
#E50 [Inicializar alfabeto]
Alfa="abcdefghijklmnopqrstuvwxyz"
#E55 [Escrever cabeçalho]
print("Texto com as palavras invertidas")
print("=")
#E60 [Inicializar posição do primeiro espaço]
Esp =texto.find(" ")
#E70 [Estabelecer ciclo para processar as palavras]
while Esp!=-1:
    #E80 [Extrair a palavra]
    Pal=texto[0:Esp]
    onde=Alfa.index(Pal[0])
    #E90 [Atualizar vetor das ocorrências]
    F[onde]=F[onde]+1
    #E100 [Inicializar palavra ao contrário]
    PC =""
    #E110 [Estabelecer ciclo para escrever palavra ao contrário]
    for i in range(len(Pal)):
        # E120 [Atualizar palavra ao contrário]
        PC=Pal[i]+PC
    #E130 [Escrever palavra ao contrário]
    print(PC)
    #E140 [Atualizar o número de palavras]
    Qt=Qt+1
    #E150 [Atualizar texto]
    texto=texto[Esp+1:len(texto)]
    #E160 [Determinar a posição do próximo espaço]
    Esp =texto.find(" ")
#E170 [Escrever o número de palavras no texto]
print("Há ",Qt, "palavras no texto ", TextoInicial, ".")
#E180 [Estabelecer ciclo para processar frequência de palavras começadas por uma dada letra]
for i in range(26):
    #E190 [Escrever ocorrência de palavras começadas por uma dada letra]
    if F[i]>0:
        print("Há", F[i], "palavras começadas por ", Alfa[i])
