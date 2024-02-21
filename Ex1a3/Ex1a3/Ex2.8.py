print("Quanto mede o primeiro lado? ")
L1=int(input())
print("Quanto mede o segundo lado? ")
L2=int(input())
print("Quanto mede o terceiro lado? ")
L3=int(input())
if L1>L2:
 if L1>L3:
    A=L1
    B=L2
    C=L3
 else:
    A = L3
    B = L2
    C = L1
elif L2>L3:
    A=L2
    B=L1
    C=L3
else:
    A = L3
    B = L2
    C = L1
if A >= B + C:
 print("Não se forma nenhum triângulo")
elif pow(A,2) == pow(B,2) + pow(C,2):
 print("Forma - se um triângulo retângulo.")
elif pow(A,2) > pow(B,2) + pow(C,2):
 print("Forma-se um triângulo obtuso")
else:
 print("Forma-se um triângulo agudo")
