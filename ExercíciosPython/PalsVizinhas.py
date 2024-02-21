# [Ler e validar o texto]
print("Qual o texto?")
texto=input()
while len(texto)==0:
    print("Qual o texto?")
    texto = input()
#"Inicializar contador de palavras]
cont=1
#Inicializar contador de palavras maiores do que vizinha
Maiores=0
texto=texto+" "
esp=texto.find(" ")
#Extrair 1º palavra]
Ant=texto[0:esp]
#Atualizar texto]
texto=texto[esp+1:len(texto)]
#[Determinar posição do 2º espaço]
esp=texto.find(" ")
while esp!=-1:
    #[Extrair palavra]
    Pal=texto[0:esp]
    #[Actualizar o número de palavras]
    cont=cont+1
    #[Actualizar texto]
    texto = texto[esp + 1:len(texto)]
    #[Determinar posição de próximo espaço]
    esp = texto.find(" ")
    # [Extrair próxima palavra]
    if esp==-1:
        Prox=texto
    else:
        Prox=texto[0:esp]
    # [Escrever se a palavra for maior do que as vizinhas e atualizar contador]
    if Pal[0] > Ant[0] and Pal[0] > Prox[0]:
        print(Pal, cont, "ª posição")
        Maiores = Maiores + 1
    # [Atualizar palavra anterior]
    Ant = Pal
# "Calcular % de palavras >s que vizinhas]
PerM = Maiores / cont * 100
# Escrever % de palavras >s que vizinhas]
print("Há ",PerM, "%,",Maiores,"/",cont, "de palavras maiores que as vizinhas")