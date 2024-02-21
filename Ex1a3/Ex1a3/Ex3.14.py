print("Qual o nome do cliente? (Fim para terminar)")
Nome=input()
while Nome!="Fim":
    Valor=0
    Iva=0
    print("Livro, CD, DVD ou Sair")
    tipo=input()
    while tipo!="Livro" and tipo!="CD" and tipo!="DVD" and tipo!="Sair":
        print("Livro, CD, DVD ou Sair")
        tipo = input()
    Num=0
    while tipo!="Sair":
        print("Valor?")
        ValorArtigo=int(input())
        while ValorArtigo<=0:
            print("Valor?")
            ValorArtigo = int(input())
        if tipo == "Livro":
            valoriva = ValorArtigo * 0.06
        else:
            valoriva = ValorArtigo * 0.23
        Valor=Valor + ValorArtigo + valoriva
        Iva=Iva + valoriva
        Num=Num + 1
        print("Livro, CD, DVD ou Sair")
        tipo = input()
        while tipo != "Livro" and tipo != "CD" and tipo != "DVD" and tipo != "Sair":
            print("Livro, CD, DVD ou Sair")
            tipo = input()
    print(Nome, "comprou", Num," artigos,")
    print("e paga ", Valor, "(sendo ", round(Iva,2), "euros de IVA)")
    print("Qual o nome do próximo cliente? (Fim para terminar)")
    Nome = input()
