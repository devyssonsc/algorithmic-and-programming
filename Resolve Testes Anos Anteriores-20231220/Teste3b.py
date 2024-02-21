vogal="aeiou"
Sozinho=[0,0,0,0,0]
Junto=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print("Qual o texto? Terminar para fim!")
texto=input()
while len(texto)==0:
 print("Qual o texto? Terminar para fim!")
 texto = input()

while texto!="Terminar":
 print(texto)
 print(" *** ")
 texto2 = texto + " "
 novotexto = ""
 Esp = texto2.find(" ")
 while Esp != -1:
     Pal = texto2[0:Esp]
     novaPal = ""
     k = 0
     Pal = Pal + " "
     while k < len(Pal):
         if vogal.find(Pal[k]) >= 0:
             if vogal.find(Pal[k + 1]) == -1:
                 novaPal = novaPal + Pal[k] + "K" + Pal[k]
                 Sozinho[vogal.find(Pal[k])] = Sozinho[vogal.find(Pal[k])] + 1
             else:
                 novaPal = novaPal + Pal[k:k + 2] + "K" + Pal[k:k + 2]
                 Junto[vogal.find(Pal[k])][vogal.find(Pal[k + 1])] = Junto[vogal.find(Pal[k])][
                                                                         vogal.find(Pal[k + 1])] + 1
                 k = k + 1
         else:
             novaPal = novaPal + Pal[k]
         k = k + 1
     print(novaPal)
     novotexto = novotexto + novaPal
     texto2 = texto2[Esp + 1:len(texto2)]
     Esp = texto2.find(" ")


 print(" *** ")
 print(novotexto)
 print("Qual o texto? Terminar para fim!")
 texto = input()
 while len(texto) == 0:
     print("Qual o texto? Terminar para fim!")
     texto = input()


print("***")
print("Vogais sozinhas")
print("***")
for i in range(5):
    if Sozinho[i]>0:
        print(vogal[i], " aparece ",Sozinho[i], "vezes")
print("***")
print("Vogais acompanhadas")
print("***")
for i in range(5):
    for j in range(5):
        if Junto[i][j]>0:
            print(vogal[i]+vogal[j], " aparece ",Junto[i][j], "vezes")