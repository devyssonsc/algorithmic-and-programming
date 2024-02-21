print("Nome? (fim para terminar)")
Nome = input()
while Nome == "":
    print("Nome? (fim para terminar)")
    Nome = input()
ab=0
nopeso=0
marginal=0
acima=0
obeso=0
MenorIMC=9999
somaIMC=0
while Nome!="fim":
    print("Qual o seu peso em kg?")
    peso = int(input())
    while peso<30 or peso>300:
        print("Qual o seu peso em kg?")
        peso = int(input())
    print("Qual a sua altura em metros?")
    altura = float(input())
    while altura<1 or altura>2.5:
        print("Qual a sua altura em metros?")
        altura = float(input())
    IMC=peso/altura**2
    print('IMC=',IMC)
    if IMC < 19.1:
        print("Abaixo do peso")
        ab=ab+1
    elif IMC < 25.8:
        print("no peso normal")
        nopeso=nopeso+1
    elif IMC < 27.3:
        print("marginalmente acima do peso")
        marginal=marginal+1
    elif IMC < 32.3:
        print("Acima do peso ideal")
        acima=acima+1
    else:
        print("Obeso")
        obeso=obeso+1
    somaIMC=somaIMC+IMC
    if IMC<MenorIMC:
        MenorIMC=IMC
        NomeMenorIMC=Nome
    print("Nome? (fim para terminar)")
    Nome = input()
    while Nome == "":
        print("Nome? (fim para terminar)")
        Nome = input()

total=ab+nopeso+marginal+acima+obeso
if total==0:
    print('Ninguem procesado')
else:
    print('Abaixo do peso', ab/total*100,'%')
    print('No peso', nopeso / total * 100, '%')
    print('Marginalmente acima do peso', acima/total*100,'%')
    print('Obeso', obeso / total * 100, '%')
    print('Menor IMC=',MenorIMC, 'do ',NomeMenorIMC)
    media=somaIMC/total
    print('Media de IMCs=',media)