#Exercício 1: Pretende-se saber o valor a pagar numa compra em que cada comprador só pode comprar um tipo de
#artigo, mas várias quantidades. Uma caneta custa 0.5, um lápis 0.25 e uma borracha custa 1 euros.
#Exemplo:
#Que artigo quer comprar? canetas
#Quantas canetas? 4
#Vai pagar 2 euros por 4 canetas.

print('Qual o tipo de artigo? Canetas,Lapis, Borracha')
Tipo = input()
print('Quantas ', Tipo,"?")
Quantas = input()
if Tipo == 'Canetas':
 Preco = 0.5 * int(Quantas)
elif Tipo == 'Lapis':
 Preco = 0.25 * int(Quantas)
else:
 Preco = int(Quantas)
print('Vai pagar ', Preco, ' euros por ', Quantas, Tipo, ",")