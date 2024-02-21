#M10 [Ler e validar o número de pessoas]
print('Quants pessoas?')
n=int(input())
while n<=0:
    print('Quantas pessoas? (Atenção tem que ser maior que zero!!!)')
    n = int(input())
#M20 [Inicializar a soma das idades]
soma=0

#M30 [Estabelecer ciclo para processar as pessoas]
for i in range(n):
    #M40 [Ler e validar a idade da pessoa]
    print('Insira a idade ]0, 150[ inteiro da pessoa n.', i+1)
    Idade=int(input())
    while Idade<=0 or Idade>150:
        print('Insira a idade ]0, 150[ inteiroda pessoa n.', i+1)
        Idade = int(input())
    # M50 [Acumular soma de idades]
    soma=soma+Idade
#M60 [Calcular media das idades]
Media=soma/n
#M70 [Escrever média das idades]
print ('Media = ',Media ,' anos.')
#M80 [Terminar]
#Exit []
