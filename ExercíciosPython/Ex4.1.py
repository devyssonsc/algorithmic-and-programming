
A=[0,0,0,0,0]
for i in range(5):
        A[i] = int(input("Qual o numero?"))
        while A[i] < 0:
            A[i] = int(input("Qual o numero? (maiot ou igual que zero pf"))

B= [0,0,0,0,0,0,0,0,0]
Qt=0
B[0]=int(input("Qual o numero? -1 para fim"))
while B[0]<-1:
    B[0] = int(input("Qual o numero? -1 para fim; ou positivos"))
while B[Qt]!=-1 and Qt<9:
    Qt=Qt+1
    B[Qt]=int(input("Qual o numero? -1 para fim"))
    while B[Qt]<-1:
        B[Qt] = int(input("Qual o numero? -1 para fim; ou positivos"))

C=[0,0,0,0,0,0,0,0,0, 0,0,0,0,0]
for i in range(5):
    C[i]=A[i]
for i in range(Qt):
    C[i+5] = B[i]
QtsC=Qt+5

D=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
D[0]=C[0]
QtsD=0
for i in range(1, QtsC):
    D[QtsD+1]=C[i]
    k=0
    while C[i] != D[k] and k < QtsD + 1:
        k=k+1
    if k == QtsD + 1:
       QtsD=QtsD+1


print("**********A*")
for i in range(5):
    print(A[i])

print("**********B*")
for i in range(Qt):
    print(B[i])

print("**********C*")
for i in range(QtsC):
    print(C[i])

print("**********D*")
for i in range(QtsD):
    print(D[i])

print("\nEscrver impares do vetor C")
if QtsC>0:
    for i in range(QtsC):
        if C[i] % 2 !=0:
            print("C[",i+1,"]=",C[i])

print("\nEscrver inverso do vetor C")
if QtsC>0:
    for i in range(QtsC-1,-1,-1):
        print('C[',i+1,']=',C[i])

i = 0
Procura = int(input("Qual o numero a procurar?"))
while Procura < 0:
   Procura = int(input("Qual o numero? (maior ou igual que zero pf"))
while Procura != C[i] and i < QtsC:
    i = i + 1
if Procura == C[i]:
    print("Encontrado na posição", i + 1)
else:
    print("Nao encontrei!")

i = 0
Procura = int(input("Escolha outro! Qual o numero a procurar?"))
while Procura < 0:
   Procura = int(input("Escolha outro!Qual o numero? (maior ou igual que zero pf"))
while Procura != C[i] and i < QtsC:
   i = i + 1
if Procura == C[i]:
   print("Encontrado na posição", i + 1)
else:
   print("Nao encontrei!")