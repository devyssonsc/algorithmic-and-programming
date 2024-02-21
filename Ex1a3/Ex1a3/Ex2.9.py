print("Qual é o nome do comprador? ")
Nome=input()
print("Qual é a marca do veículo? ")
MArca=input()
print("Qual é o modelo do veículo? ")
Modelo=input()
print("Qual é cilindrada do motor? ")
cc=int(input())
if cc<1250:
 IA=3.74*cc-2417.56
else:
 IA=8.86*cc- 8813.22
print("IA=",IA)