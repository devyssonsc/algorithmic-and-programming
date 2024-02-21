Maius = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
Minus= "abcdefghijklmnopqrstuvwxyz"
Artigo = input("Qual a descrição do artigo? ")
while len(Artigo) == 0:
    print("Não são aceites descrições vazias!")
    Artigo = input("Qual a descrição do artigo? ")
esp=Artigo.find(" ")
Artigo=Artigo+" "
NovoArtigo=""
while esp!=-1:
    pal=Artigo[0:esp]
    prim=pal[0]
    if Maius.find(prim)==-1:
        if Minus.find(prim)>=0:
            pal=Maius[Minus.find(prim)]+pal[1:len(pal)]
        else:
            pal="*"+pal[1:len(pal)]
    for y in range(1,len(pal)):
        car= pal[y]
        if Minus.find(car) == -1:
            if Maius.find(car) >= 0:
                pal = pal[0:y]+Minus[Maius.find(car)] + pal[y+1:len(pal)]
            else:
                pal = pal[0:y]+"#" + pal[y+1:len(pal)]
    NovoArtigo=NovoArtigo+pal+"_"
    Artigo=Artigo[esp+1:len(Artigo)]
    esp = Artigo.find(" ")
NovoArtigo=NovoArtigo[0:len(Artigo)-1]
print("***")
print("Nova descrição: ",NovoArtigo)
