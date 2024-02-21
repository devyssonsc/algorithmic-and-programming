print("Qual o texto?")
Texto=input()
while len(Texto)==0:
    print("Qual o texto?")
    Texto = input()
Txt=Texto+" "
esp=Txt.find(" ")
while esp>=0:
    print(Txt[0:esp])
    Txt= Txt[esp+1: len(Txt)]
    esp = Txt.find(" ")

