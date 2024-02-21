#Exercício 8: O IMC, Índice de Massa Corpórea, é uma medida para se determinar a condição física de uma pessoa. Para
#fazer o cálculo do IMC basta dividir seu peso em kg pela altura ao quadrado: 𝐼𝑀𝐶 = 𝑃𝑒𝑠𝑜 𝑒𝑚 𝑘𝑔 /𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑚 𝑚 𝑥
#a𝑙𝑡𝑢𝑟𝑎 𝑒𝑚 𝑚 . Para uma pessoa com o peso 85kg e uma altura de 1.65: 𝐼𝑀𝐶 = 85 /1.65𝑥1.65 = 31.2. Calcule o IMC de
#uma pessoa, sabendo o seu peso e altura.
#Exemplo com DATA 85, 1.65
#Qual o peso? 85
#Qual a altura? 1.65
#IMC = 31.2

print ("Qual o peso?")
peso = int(input())
print ("Qual a altura? (cm)")
altura = int(input())
IMC=peso/(altura*altura)*10000
print ("IMC",IMC )