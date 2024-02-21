Contador=0
print("Introduza o numero do aluno: (0 para fim)")
num=int(input())
while num<0:
    print("Introduza o numero do aluno: (0 para fim)")
    num = int(input())
while num != 0:
    Contador=Contador +1
    print("Quantas ucs fez o aluno ", num, " (1 a 5)")
    qtucs=int(input())
    while qtucs <= 0 or qtucs > 5:
        print("Quantas ucs fez o aluno ", num, " (1 a 5)")
        qtucs = int(input())
    Soma=0
    for i in range(qtucs):
        print("Qual das ucs?")
        print("(A)lgoritmia, A(R)quitetura")
        print("(O)ficinas, (M)atemática, Or(G)anização")
        uc=input()
        while uc!= "A" and uc != "R" and uc !="O" and uc != "M" and uc != "G":
            print("Qual das ucs?")
            print("(A)lgoritmia, A(R)quitetura")
            print("(O)ficinas, (M)atemática, Or(G)anização")
            uc = input()
        print("Qual a nota da uc?")
        nota=float(input())
        while nota < 0 or nota > 20:
            print("Qual a nota da uc?")
            nota = float(input())
        Soma=Soma + nota
    Media = Soma/qtucs
    print("O aluno ",num, " fez ",qtucs, " uc com uma média de ",Media)
    print("Introduza o numero do aluno: (0 para fim)")
    num = int(input())
    while num < 0:
        print("Introduza o numero do aluno: (0 para fim)")
        num = int(input())
if Contador==0:
 print("Ninguém")
else:
 print("Nº de alunos processados: ",Contador)