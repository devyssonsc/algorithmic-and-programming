print ("************Inicio programa**************")
print("Nome do comprador? (terminar para fim)")
cliente = input()
while cliente != "terminar":
    print ("***********Inicio ", cliente, "***********")
    print ("Quantas bebidas diferentes quer?")
    n=int(input())
    while n<=0:
        print("Quantas bebidas diferentes quer?")
        n = int(input())
    total=0
    ivas=0
    for i in range(n):
        print ("Bebida? (A)guas, (C)erveja, (I)ogurtes, (L)eite, (R)efrigerantes, (V)inho ?")
        tipo=input()
        while tipo!="A" and tipo!="C" and tipo!="I" and tipo!="L" and tipo!="R" and tipo!="V":
            print("Bebida? (A)guas, (C)erveja, (I)ogurtes, (L)eite, (R)efrigerantes, (V)inho ?")
            tipo = input()
        print ("Preco unitário?")
        unit=float(input())
        while unit<=0:
            print("Preco unitário?")
            unit = float(input())
        print("Quantidade?")
        qt=int(input())
        while qt<=0:
            print("Quantidade?")
            qt = int(input())
        sIVA=unit*qt
        if tipo=="A" or tipo=="V":
            tipoIVA=0.13
        elif tipo=="C" or tipo=="R":
            tipoIVA=0.23
        else:
            tipoIVA=0.06
    ivaItem=tipoIVA*sIVA
    total = total + sIVA +ivaItem
    ivas = ivas + ivaItem
    print("Item:", sIVA, "(+iva", tipoIVA * 100, "% de ", ivaItem, ")")
    print("Paga:", total, "(sendo o iva ", ivas, ")")
    print("************Fim", cliente, "**************")
    print("Nome do comprador? (terminar para fim)")
    cliente = input()
print("************Fim programa**************")
