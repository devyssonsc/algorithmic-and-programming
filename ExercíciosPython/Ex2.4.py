print("Qual a nota da disciplina 1?")
dis1 = int(input())

print("Qual a nota da disciplina 2?")
dis2 = int(input())

print("Qual a nota da disciplina 3?")
dis3 = int(input())

notaFinal = (dis1 + dis2 + dis3) / 3
print("a nota final do aluno é", notaFinal)

if notaFinal >= 10:
    print("Aprovado")
else:
    print("Reprovado")