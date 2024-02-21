veiculos = ["","","","","","","","","","","","","","","","","","","",""]
freqVeiculos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

matricula = input("Introduza a matrícula")
while matricula == "":
    matricula = input("Introduza a matrícula")

contaMatriculas = 0
veiculosDiferentes = 0

while matricula != "ZZ-ZZ-ZZ":

    if len(matricula) != 8:
            print("Número de caracteres errado")
    else:
        diferentes = 0

        tipos = [0,0,0]

        primeiros = matricula[0] + matricula[1]

        if (alfa.find(primeiros[0]) != -1) != (alfa.find(primeiros[1]) != -1) or (numeros.find(primeiros[0]) != -1) != (
                numeros.find(primeiros[1]) != -1):
            diferentes = 1
        else:
            if (alfa.find(primeiros[0]) != -1) == True:
                tipos[0] = 1
            else:
                tipos[0] = 2

        segundos = matricula[3] + matricula[4]

        if (alfa.find(segundos[0]) != -1) != (alfa.find(segundos[1]) != -1) or (numeros.find(segundos[0]) != -1) != (
                numeros.find(segundos[1]) != -1):
            diferentes = 2
        else:
            if (alfa.find(segundos[0]) != -1) == True:
                tipos[1] = 1
            else:
                tipos[1] = 2

        terceiros = matricula[6] + matricula[7]

        if (alfa.find(terceiros[0]) != -1) != (alfa.find(terceiros[1]) != -1) or (numeros.find(terceiros[0]) != -1) != (
                numeros.find(terceiros[1]) != -1):
            diferentes = 3
        else:
            if (alfa.find(terceiros[0]) != -1) == True:
                tipos[2] = 1
            else:
                tipos[2] = 2

        temLetra = False
        temNumero = False
        qtHifen = 0

        for i in range(len(matricula)):
            if alfa.find(matricula[i]) != -1:
                temLetra = True
            if numeros.find(matricula[i]) != -1:
                temNumero = True
            if matricula[i] == "-":
                qtHifen += 1

        if qtHifen != 2:
            print("Não tem 2 traços")
        elif temNumero == False or temLetra == False:
            print("Não existe esse tipo de matrícula")
        elif primeiros.find("-") != -1 or segundos.find("-") != -1 or terceiros.find("-") != -1:
            print("Não tem traços certos")
        elif diferentes != 0:
            print("Os dois", diferentes, "ºs caracteres são de tipos diferentes")
        else:
            qualTipo = ""
            for j in range(3):
                qualTipo += str(tipos[j])

            if qualTipo == "122":
                print("Tipo 1")
            elif qualTipo == "221":
                print("Tipo 2")
            elif qualTipo == "212":
                print("Tipo 3")
            else:
                print("Tipo 4")

            ql = 0
            while veiculos[ql] != matricula and ql < contaMatriculas:
                ql += 1

            if ql < contaMatriculas:
                freqVeiculos[ql] += 1
            else:
                veiculos[ql] = matricula
                freqVeiculos[ql] = 1
                veiculosDiferentes += 1

        contaMatriculas += 1

    matricula = input("Introduza a matrícula")
    while matricula == "":
        matricula = input("Introduza a matrícula")

print("*** Fim do dia ***")

for v in range(veiculosDiferentes):
    for m in range(veiculosDiferentes):
        if veiculos[v] < veiculos[m]:
            veiculos[v], veiculos[m] = veiculos[m], veiculos[v]
            freqVeiculos[v], freqVeiculos[m] = freqVeiculos[m], freqVeiculos[v]

for vo in range(veiculosDiferentes):
    print(veiculos[vo], "entrou", freqVeiculos[vo], "vezes")