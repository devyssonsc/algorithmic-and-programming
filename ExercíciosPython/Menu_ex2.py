listaClientes = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",]
listaOrcamentos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

contaClientes = 0

nomeCliente = input("Nome do cliente? ")
while nomeCliente == "":
    nomeCliente = input("Nome do cliente? ")

while nomeCliente != "Exit":
    tipoMenu = input("Tipo de menu? (I)nfantil, (V)egetariano, (P)eixe, (C)arne, E(x)it")
    while tipoMenu != "I" and tipoMenu != "V" and tipoMenu != "P" and tipoMenu != "C" and tipoMenu != "x":
        tipoMenu = input("Tipo de menu? (I)nfantil, (V)egetariano, (P)eixe, (C)arne, E(x)it")

    valorSemIVA = 0

    while tipoMenu != "x":
        qt = int(input("Quantidade? "))

        if tipoMenu == "I":
            valorSemIVA += qt * 10
        elif tipoMenu == "V":
            valorSemIVA += qt * 18
        elif tipoMenu == "P":
            valorSemIVA += qt * 15
        else:
            valorSemIVA += qt * 12

        tipoMenu = input("Tipo de menu? (I)nfantil, (V)egetariano, (P)eixe, (C)arne, E(x)it")
        while tipoMenu != "I" and tipoMenu != "V" and tipoMenu != "P" and tipoMenu != "C" and tipoMenu != "x":
            tipoMenu = input("Tipo de menu? (I)nfantil, (V)egetariano, (P)eixe, (C)arne, E(x)it")

    print(nomeCliente, "pagará", valorSemIVA * 1.23, "euros (", valorSemIVA, "+", valorSemIVA * 0.23, "de IVA)")

    listaClientes[contaClientes] = nomeCliente
    listaOrcamentos[contaClientes] = valorSemIVA * 1.23

    contaClientes += 1

    nomeCliente = input("Nome do cliente? ")
    while nomeCliente == "":
        nomeCliente = input("Nome do cliente? ")

for i in range(contaClientes):
    for j in range(contaClientes):
        if listaOrcamentos[i] > listaOrcamentos[j]:
            listaOrcamentos[i], listaOrcamentos[j] = listaOrcamentos[j], listaOrcamentos[i]
            listaClientes[i], listaClientes[j] = listaClientes[j], listaClientes[i]

print("O orçamento mais elevado é o do", listaClientes[0], "=", listaOrcamentos[0])