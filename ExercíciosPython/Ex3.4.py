#Ler e validar nome do primeiro proprietário
print("Nome do proprietário ('terminar' para fim: ")
prop = input()
while prop == "":
    print("Nome do proprietário ('terminar' para fim: ")
    prop = input()
#estabelecer ciclo para processar carros
while prop != 'terminar':
    #Ler e validar cilindrada
    print("Cilindrada do veículo: ")
    cc = int(input())
    while cc == 0:
        print("Cilindrada do veículo: ")
        cc = int(input())
    #Calcular IA
    ia = 0
    if cc <= 1250:
        ia = 3.74 * cc - 2417.56
    else:
        ia = 8.86 * cc - 8813.22
    print("O", prop, "terá que pagar um imposto de ", ia, " Euros")
    #Ler e validar nome do próximo proprietário
    print("Nome do proprietário ('terminar' para fim: ")
    prop = input()
    while prop == "":
        print("Nome do proprietário ('terminar' para fim: ")
        prop = input()