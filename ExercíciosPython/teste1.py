VetorPal = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
VetorOc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
NPDCT=0
VetorPalCV = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
VetorOcCV = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
NPDCV=0
print("Qual o texto?")
texto=input()
while len(texto)==0:
    print("Qual o texto?")
    texto = input()
print("Qual a letra?")
letra=input()
while len(letra)==0:
    print("Qual a letra?")
    letra = input()
#Inicializar o numero de palavras começadas e terminadas por letra
PCT=0
vogais="aeiou"
PCV=0
texto2=texto+" "
#V40 [Inicializar contador de palavras]
Cont=0
#V50 [Determinar primeiro espaço]
Esp=texto2.find(" ")
#V60 [Estabelecer ciclo para processar palavras]
while Esp!=-1:
    Pal = texto2[0:Esp]
    print(Pal)
    if Pal[0]==Pal[len(Pal)-1] and Pal[0]==letra:
        PCT=PCT+1
        VetorPal[NPDCT] = Pal
        VetorOc[NPDCT] = 1
        j = 0
        while VetorPal[j] != Pal:
            j = j + 1
        if j == NPDCT:
            NPDCT = NPDCT + 1
        else:
            VetorOc[j] = VetorOc[j] + 1
    if vogais.find(Pal[0])>=0:
        PCV = PCV+1
        VetorPalCV[NPDCV] = Pal
        VetorOcCV[NPDCV] = 1
        j = 0
        while VetorPalCV[j] != Pal:
            j = j + 1
        if j == NPDCV:
            NPDCV = NPDCV + 1
        else:
            VetorOcCV[j] = VetorOcCV[j] + 1
    Cont=Cont+1
    texto2 = texto2[Esp + 1:len(texto2)]
    Esp = texto2.find(" ")
print("Em ", texto, " há ", Cont, " palavras")
print("Em ", texto, " há ", PCT, " palavras começadas e terminadas por", letra)
palsdif=""
for i in range(NPDCT):
    palsdif=palsdif+VetorPal[i]+","
print("Dessas, ",NPDCT,"Palavras diferentes(",palsdif[0:len(palsdif)-1],")")
print("Em ", texto, " há ", PCV, " palavras começadas por vogais")
palsdif=""
for i in range(NPDCV):
    palsdif=palsdif+VetorPalCV[i]+","
print("Dessas, ",NPDCV,"Palavras diferentes(",palsdif[0:len(palsdif)-1],")")
