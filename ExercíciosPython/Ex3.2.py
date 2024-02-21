#Algoritmo MediaIdadesDesconhecido
#Este algoritmo, dadas as idades de um número desconhecido de pessoas, calcula e escreve a média dessas idades.
#M10 [Inicializar a soma das idades]
Soma=0
#M20 [Inicializar o número de pessoas]
N=0
#M30 [Ler e validar a idade da 1ª pessoa]
print('Insira a idade (0 para fim)')
Idade=int(input())
while Idade < 0 or Idade>150:
    print('Insira a idade (0 para fim)')
    Idade = int(input())
#M40 [Estabelecer ciclo para processar as pessoas]
while Idade!=0:
    #M50 [Acumular soma de idades]
    Soma=Soma+Idade
    #M60 [Atualizar o número de pessoas]
    N=N+1
    #M70 [Ler e validar a idade da próxima pessoa]
    print('Insira a idade (0 para fim)')
    Idade = int(input())
    while Idade < 0 or Idade>150:
        print('Insira a idade (0 para fim)')
        Idade = int(input())
#M80 [Calcular e escrever a media das idades]
if N==0:
    print('Ninguém processado')
else:
    Media=Soma/N
    print ('Media = ',Media ,' anos')
#M90 [Terminar]