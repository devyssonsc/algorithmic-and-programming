#Ler e validar um texto
print("Qual o texto?")
Texto=input()
while len(Texto)==0:
 print("Qual o texto?")
 Texto = input()
#Dado um texto contar o número de vezes que cada letra ocorre.
#Inicializar vetor das frequencias
L=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Inicializar as letras "possiveis"
alfa="abcdefghijklmnopqrstuvwxyz"
#Determinar o tamanho do taxto
tam=len(Texto)
#Estabelecer um ciclo para processar as letras
for i in range(tam):
 #Extrair cada letra
 letra= Texto[i]
 # Encontrar a letra nas letras "possiveis"
 onde = alfa.find(letra)
 # Atualizar vetor das frequencias caso a letra seja uma das "possiveis"
 if onde >= 0:
     L[onde] = L[onde] + 1
# Estebelecer um ciclo para processar todas a letras do alfabeto
for i in range(len(alfa)):
    # Se essa letra existe no texto
    if L[i] > 0:
        print(alfa[i], "ocorre ", L[i], "vezes")