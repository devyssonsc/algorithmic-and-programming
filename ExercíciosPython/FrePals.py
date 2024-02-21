#Inicializar vetor das palavras diferentes
Pw=["","","","","","","","","","","","","","","","","","",""]
#Incializar vetor das frequencias das palaras diferentes
F=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Ler e validar o texto
print("Qual o texto?")
Texto=input()
while len(Texto)==0:
    print("Qual o texto?")
    Texto = input()
#Incializar o novotexto com o texto e um espaço no fim
NovoTxt=Texto+" "
#Inializar o numero de palavras diferentes
numPals = 0
#Procurar o primeiro espaço do texto
esp=NovoTxt.find(" ")
#Enquanto houver espaços
while esp>=0:
    #Estrair palavrara
    pal = NovoTxt[0:esp]
    # Colocar apalvara no fim do vetor de palavras e ocorrencia a 1
    Pw[numPals] = pal
    F[numPals] = 1
    # Ver se a palavra já existia
    j = 0
    while Pw[j] != pal:
        j = j + 1
    # Se a palavra nao existia, entao incrementar o numero de palavras diferentes
    # Senao atualizar a frequencia dessa palavra
    if j == numPals:
        numPals = numPals + 1
    else:
        F[j] = F[j] + 1
    #Atualizar texto
    NovoTxt= NovoTxt[esp+1: len(NovoTxt)]
    #Encontrar o primeiro espaço do novo texto
    esp = NovoTxt.find(" ")
    #Escrever o numero de palavras diferentes
    print (Texto, "tem ", numPals, " palavras diferentes ")
#Escrever cada palavra e respetiva ocorrencia
for i in range(numPals):
    print( Pw[i]," ocorre ", F[i], "vezes")