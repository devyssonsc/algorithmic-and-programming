#[Inicializar o menor f(x)]
Menor=999999
#[Ler e validar o limite inferior]
print("Qual o Limite inferior? (21 para terminar) ")
LimiteInf = int(input())
while LimiteInf < -20 or LimiteInf>21:
    print("Qual o Limite inferior? (21 para terminar) ")
    LimiteInf = int(input())
#[Estabelecer ciclo para processar os intervalos]
while LimiteInf!=21:
    #[Inicializar soma de f(x) deste intervalo]
    soma=0
    #[Inicializar contador de x deste intervalo]
    conta=0
    #[Ler e validar o limite superior]
    print("Qual o Limite superior?  ")
    LimiteSup= int(input())
    while LimiteSup <= LimiteInf or LimiteSup > 20:
        print("Qual o Limite superior?  ")
        LimiteSup = int(input())
    #[Estabelecer um ciclo para processar o x]
    for x in range (LimiteInf, LimiteSup+1):
        #[Calcular F(x)]
        if x<0:
            if x % 2 ==0:
                Fx=3.14/x
            else:
                Fx=abs(2*x)
        elif x % 2 ==0:
                Fx=1
                for i in range(x,1,-1):
                    Fx = Fx*i
                Fx=2*Fx
        else:
            Fx=0
            for i in range(1, x+1):
                Fx = Fx+i
        #[Escrever F(x)]
        print('F(',x,')=',Fx)
        #[Atualizar soma de f(x)
        soma=soma+Fx
        #[Incrementar contador de x]
        conta=conta+1
        #[Atualizar F(x) menor e respetivo x]
        if Fx<Menor:
            Menor=Fx
            MenorX=x
    #[Calcular media de f(x) do intervalo]
    media=soma/conta
    #[Escrever media de f(x) deste intervalo
    print("Media de f(x), intervalo [",LimiteInf,",",LimiteSup,"]=", media)
    # [Ler e validar o limite inferior do próximo intervalo]
    print("*****")
    print("Qual o Limite inferior? (21 para terminar) ")
    LimiteInf = int(input())
    while LimiteInf < -20 or LimiteInf > 21:
        print("Qual o Limite inferior? (21 para terminar) ")
        LimiteInf = int(input())
#[Escrever menor f(x) e respetivo x
if Menor!=999999:
    print("O menor f(x)=f(",MenorX,")=",Menor)

