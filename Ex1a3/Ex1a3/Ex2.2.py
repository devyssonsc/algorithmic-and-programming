print('Qual o tipo de artigo? Canetas, Lapis, Borracha')
Tipo = input()
print('Quantas ', Tipo,"?")
Quantas = input()
if Tipo == 'Canetas':
 Preco = 0.5 * int(Quantas)
elif Tipo == 'Lapis':
 Preco = 0.25 * int(Quantas)
else:
 Preco = int(Quantas)
if int(Quantas) > 100 :
 Preco = Preco *0.75
 cliente='Excelente'
elif int(Quantas) > 10:
 Preco = Preco * 0.9
 cliente = 'Bom'
else:
 cliente = ''
if cliente != '' :
 print('Vai pagar ', Preco, 'euros por ',Quantas, Tipo,',',
cliente,' cliente')
else:
 print('Vai pagar ', Preco, 'euros por ',Quantas, Tipo)
