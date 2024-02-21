#Exercício 3: Dados o nome e idade de dois irmãos, calcular a média das suas idades, dizendo qual deles é o mais velho
#e qual a diferença de idades entre os dois.
#Exemplo:
#Qual é o nome do 1º Irmão? João
#Qual é a idade do 1ºIrmão? 18
#Qual é o nome do 2ºIrmão? Pedro
#Qual é a idade do 2ºIrmão? 15
#Média =16.5 anos.
#Diferença =3
#Pedro Mais velho
print('Qual é o nome do 1º Irmão?')
Nome1 = input()
print('Qual a idade do primeiro irmao?')
Idade1 = int(input())
print('Qual é o nome do 2º Irmão?')
Nome2 = input()
print('Qual a idade do segundo irmao?')
Idade2 = int(input())
media = float((Idade1+Idade2)/2)
print('Media=', media, 'anos.')
dif=abs(Idade1-Idade2)
print('Diferença =',dif )
if Idade1>Idade2:
    print(Nome1,'mais velho')
elif Idade1==Idade2:
    print('Gemeos')
else:
    print(Nome2, 'mais velho')
