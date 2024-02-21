nomeCliente = input("Nome do cliente? ")
while nomeCliente == "":
    nomeCliente = input("Nome do cliente? ")

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
