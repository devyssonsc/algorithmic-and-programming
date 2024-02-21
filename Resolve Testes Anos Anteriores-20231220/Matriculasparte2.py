


def NumTracos(mat):
    qt=0
    onde=mat.find("-")
    while onde!=-1:
        mat=mat[onde+1:len(mat)]
        qt=qt+1
        onde = mat.find("-")
    return (qt)

def saoNums(dup):
    return(numeros.find(dup[0])>=0 and numeros.find(dup[1])>=0)

def saoLetras(dup):
    return(letras.find(dup[0])>=0 and letras.find(dup[1])>=0)


Entrada = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
Oc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num=0
numeros="0123456789"
letras="ABCDEFGHIJKLMNOPQRSTUVXYZ"
print("Introduza a matricula")
mat=input()
while mat=="":
    print("Introduza a matricula")
    mat = input()
while mat!="ZZ-ZZ-ZZ":
    if len(mat) != 8:
        print("Número de caracteres errado")
    else:
        quantosTr = NumTracos(mat)
        if quantosTr != 2:
            print("Nao tem 2 traços")
        else:
            traco1 = mat[2]
            traco2 = mat[5]
            if traco1 != "-" or traco2 != "-":
                print("Não tem traços certos")
            else:
                dup1 = mat[0:2]
                if not saoLetras(dup1) and not saoNums(dup1):
                    print("Oa dois 1ºs carateres são de tipos diferentes")
                else:
                    dup2 = mat[3:5]
                    if not saoLetras(dup2) and not saoNums(dup2):
                        print("Os dois 2ºs carateres são de tipos diferentes")
                    else:
                        dup3 = mat[6:8]
                        if not saoLetras(dup3) and not saoNums(dup3):
                            print("Os dois 3ºs carateres são de tipos diferentes")
                        else:
                            Entrada[num] = mat
                            Oc[num] = 1
                            j = 0
                            while Entrada[j] != mat:
                                j = j + 1
                            if j == num:
                                num = num + 1
                            else:
                                Oc[j] = Oc[j] + 1
                            if saoLetras(dup1) and saoNums(dup2):
                                if saoLetras(dup3):
                                    print("Tipo 4")
                                else:
                                    print("Tipo 1")

                            elif saoNums(dup1):
                                if saoLetras(dup2) and saoNums(dup3):
                                    print("Tipo 3")

                                elif saoLetras(dup3) and saoNums(dup2):
                                    print("Tipo 2")

                                else:
                                    print("Ainda nao existe esse tipo de matricula")
                            else:
                                print("Ainda nao existe esse tipo de matricula")

    print("Introduza a matricula")
    mat = input()
    while mat == "":
        print("Introduza a matricula")
        mat = input()

print("*** Fim do dia ***")
for i in range(num):
    print(Entrada[i] ,"entrou",Oc[i], "vezes")

for y in range(num-1):
    for u in range(y+1,num):
        if Oc[y]<Oc[u]:
            troca=Entrada[y]
            Entrada[y]=Entrada[u]
            Entrada[u]=troca
            novatroca=Oc[y]
            Oc[y]=Oc[u]
            Oc[u]=novatroca

print("Ordenado agora")
print("*** Fim do dia ***")
for i in range(num):
    print(Entrada[i] ,"entrou",Oc[i], "vezes")