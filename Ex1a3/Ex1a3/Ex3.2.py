soma=0
pessoas=0
print ("Qual a idade da 1ª pessoa? ]0, 150[ inteiro(0 para fim)")
Idade=int(input())
while (Idade<0 or Idade>150):
    print("Insira a idade ]0, 150[ inteiro)0 para fim)")
    Idade = int(input())
while Idade != 0:
    soma=soma+Idade
    pessoas=pessoas+1
    print ('Qual a idade da ', pessoas+1, 'º pessoa? ]0, 150[ inteiro(0 para fim)')
    Idade=int(input())
    while (Idade<0 or Idade>150):
        print("Insira a idade ]0, 150[ inteiro)0 para fim)")
        Idade = int(input())
if pessoas>0:
    Media = soma/pessoas
    print("Media das idades =", Media, "anos")
else:
    print('Niguem processado')