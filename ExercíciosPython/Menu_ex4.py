listaClientes = ["","","","","","","","","",""]
listaOrcamentosComIVA = [0,0,0,0,0,0,0,0,0,0]
listaOrcamentosComIVAPorExtenso = ["","","","","","","","","",""]
listaOrcamentosSemIVA = [0,0,0,0,0,0,0,0,0,0]

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

    listaClientes[contaClientes] = nomeCliente
    listaOrcamentosComIVA[contaClientes] = round(valorSemIVA * 1.23, 1)
    listaOrcamentosSemIVA[contaClientes] = round(valorSemIVA, 1)

    porExtenso = ""
    aux = str(round(listaOrcamentosComIVA[contaClientes], 1))
    for e in range(len(aux)):
        if aux[e] == "1":
            porExtenso += "um "
        elif aux[e] == "2":
            porExtenso += "dois "
        elif aux[e] == "3":
            porExtenso += "três "
        elif aux[e] == "4":
            porExtenso += "quatro "
        elif aux[e] == "5":
            porExtenso += "cinco "
        elif aux[e] == "6":
            porExtenso += "seis "
        elif aux[e] == "7":
            porExtenso += "sete "
        elif aux[e] == "8":
            porExtenso += "oito "
        elif aux[e] == "9":
            porExtenso += "nove "
        elif aux[e] == "0":
            porExtenso += "zero "
        elif aux[e] == ".":
            porExtenso += "ponto "

    listaOrcamentosComIVAPorExtenso[contaClientes] = porExtenso

    print(listaClientes[contaClientes], "pagará", listaOrcamentosComIVAPorExtenso[contaClientes], "euros (",
          listaOrcamentosSemIVA[contaClientes], "+",
          round(listaOrcamentosComIVA[contaClientes] - listaOrcamentosSemIVA[contaClientes],1), "de IVA)")

    contaClientes += 1

    nomeCliente = input("Nome do cliente? ")
    while nomeCliente == "":
        nomeCliente = input("Nome do cliente? ")

for i in range(contaClientes):
    for j in range(contaClientes):
        if listaOrcamentosComIVA[i] > listaOrcamentosComIVA[j]:
            listaOrcamentosComIVA[i], listaOrcamentosComIVA[j] = listaOrcamentosComIVA[j], listaOrcamentosComIVA[i]
            listaOrcamentosSemIVA[i], listaOrcamentosSemIVA[j] = listaOrcamentosSemIVA[j], listaOrcamentosSemIVA[i]
            listaOrcamentosComIVAPorExtenso[i], listaOrcamentosComIVAPorExtenso[j] = listaOrcamentosComIVAPorExtenso[j], listaOrcamentosComIVAPorExtenso[i]
            listaClientes[i], listaClientes[j] = listaClientes[j], listaClientes[i]

print("O orçamento mais elevado é o do", listaClientes[0], "=", listaOrcamentosComIVAPorExtenso[0])
print("***Orçamentos***")
for cliente in range(contaClientes):
    print(listaClientes[cliente], "pagará", listaOrcamentosComIVAPorExtenso[cliente], "euros (", listaOrcamentosSemIVA[cliente], "+", round(listaOrcamentosComIVA[cliente] - listaOrcamentosSemIVA[cliente], 1), "de IVA)")

