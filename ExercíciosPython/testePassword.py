alfaMinus = "abcdefghijklmnopqrstuvwxyz "
alfaMaius = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
algarismos = "0123456789 "
sinais = "!@#$%&*£¢? "

password = input("Introduza a password: ")
while password == "":
    password = input("Introduza a password: ")

while password != "Game Over":

    novaPassword = password + "-"

    #Processamento
    nivelSeg = 0
    temMaiuscula = False
    temMinuscula = False
    temAlgarismo = False
    temSinal = False
    contaCarac = 0
    temEspaco = False

    for i in range(len(novaPassword)):
        if novaPassword[i] == " ":
            temEspaco = True
        else:
            if alfaMaius.find(novaPassword[i]) != -1:
                temMaiuscula = True
                #nivelSeg += 25
                if novaPassword[i+1] == alfaMaius[alfaMaius.find(novaPassword[i])+1]:
                    nivelSeg -= 10
                if novaPassword[i+1] == novaPassword[i]:
                    nivelSeg -= 20

            if alfaMinus.find(novaPassword[i]) != -1:
                temMinuscula = True
                #nivelSeg += 25
                proximaPosMinus = alfaMinus[alfaMinus.find(novaPassword[i])+1]
                if novaPassword[i+1] == proximaPosMinus:
                    nivelSeg -= 10
                if novaPassword[i+1] == novaPassword[i]:
                    nivelSeg -= 20

            if algarismos.find(novaPassword[i]) != -1:
                temAlgarismo = True
                #nivelSeg += 25
                if novaPassword[i+1] == algarismos[algarismos.find(novaPassword[i])+1]:
                    nivelSeg -= 10
                if novaPassword[i+1] == novaPassword[i]:
                    nivelSeg -= 20

            if sinais.find(novaPassword[i]) != -1:
                temSinal = True
                #nivelSeg += 25
                if novaPassword[i+1] == novaPassword[i]:
                    nivelSeg -= 20


        contaCarac += 1


    if contaCarac < 6 or contaCarac > 12:
        print("Número de caracteres errado")
    elif temEspaco == True:
        print("Não pode ter espaços")
    else:
        #Resposta
        if temMaiuscula:
            nivelSeg += 25
        if temMinuscula:
            nivelSeg += 25
        if temAlgarismo:
            nivelSeg += 25
        if temSinal:
            nivelSeg += 25
        print("***")
        print(password)
        print("Nível de segurança: ", nivelSeg, "%")

    #Pergunta denovo
    password = input("Introduza a password: ")
    while password == "":
        password = input("Introduza a password: ")