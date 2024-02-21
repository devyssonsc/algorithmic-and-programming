print("Qual a nota da disciplina 1? ")
Nota1=int(input())
print("Qual a nota da disciplina 2? ")
Nota2=int(input())
print("Qual a nota da disciplina 3? ")
Nota3=int(input())
media=float((Nota1+Nota2+Nota3)/3)
print("A nota final do aluno é ", media)
if media> 9.45:
 print("Aprovado")
else:
 print("Reprovado")