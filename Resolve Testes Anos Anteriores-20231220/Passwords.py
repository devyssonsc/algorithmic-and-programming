def contem(inicial, password):
    j=0
    while j<len(password)-1 and inicial.find(password[j])==-1:
        j=j+1
    if inicial.find(password[j]) == -1:
        return(0)
    else:
        return(1)

def VeRepete(password):
    repts=0
    for i in range(len(password)-1):
        if password[i]==password[i+1]:
            repts=repts+1
    return(repts)

def Cont(inicial, password):
    nc=0
    for i in range(len(inicial)-1):
        for j in range(len(password)-1):
            if inicial[i:i+2]==password[j:j+2]:
                nc=nc+1
    return (nc)

print("Introduza a password")
passw=input()
while passw=="":
    print("Introduza a password")
    passw = input()

if len(passw)<6 or len(passw)>12:
    print("Número de caracteres errado")
else:
    if passw.find(" ")!=-1:
        print("Não pode ter espaços")
    else:
        qt=0
        qt = qt + 25*contem("0123456789", passw)
        qt = qt + 25*contem("ABCDEFGHIJKLMNOPQRSTUVXYZ", passw)
        qt = qt + 25*contem("abcdefghijklmnopqrstuvxyz", passw)
        qt = qt + 25*contem("@!?#£$*$&€", passw)
        qt = qt - 20 *VeRepete(passw)
        qt = qt - 10*Cont("0123456789",passw)
        qt = qt - 10*Cont("ABCDEFGHIJKLMNOPQRSTUVXYZ", passw)
        qt = qt - 10*Cont("abcdefghijklmnopqrstuvxyz", passw)
        if qt<0:
            qt=0
        print("Nivel de segurança=",qt,"%")