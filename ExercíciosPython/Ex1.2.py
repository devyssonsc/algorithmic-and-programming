#Exercício 2: Pretende-se saber o valor a pagar por um determinado número de canetas,
#sabendo que cada uma custa um valor desconhecido.
#Exemplo com DATA 4, 0.5
#Quantas canetas? 4
#Quanto custa cada caneta? 0.5
#Vai pagar 2 euros por 4 canetas.

print('Quantas canetas?')
Canetas=int(input())
print('Quanto vai pagar por ', Canetas, 'Canetas?')
Preco=float(input())
Paga=Preco*Canetas
print('Vai pagar ',Paga, 'euros por ', Canetas,'canetas')
