#Ler e validar nome do proprietário
print("Nome do proprietário: ")
prop = input()
while prop == "":
    print("Nome do proprietário: ")
    prop = input()

#Ler e validade cilindrada
print("Cilindrada do veículo: ")
cc = int(input())
while cc == 0:
    print("Cilindrada do veículo: ")
    cc = int(input())

#Calcular Imposto
ia = 0
if cc <= 1250:
    ia = 3.74 * cc - 2417.56
else:
    ia = 8.86 * cc - 8813.22

#Escrever imposto
print("O", prop, "terá que pagar um imposto de ", ia," Euros")

#Terminar