#Este algoritmo, dado uma frase, calcula e escreve as suas letras.
#L10 [Inicializar alfabeto]
alfa="abcdefghijklmnopqrstuvwxyz"
#L20 [Ler e validar frase]
print("Qual o texto?")
Texto=input()
while len(Texto)==0:
    print("Qual o texto?")
    Texto = input()
# L35 [Calcular tamanho do texto]
tam=len(Texto)
# L30 [Establecer ciclo para processar carateres da frase]
for i in range(tam):
    #L40[Extrair caracter]
    letra = Texto[i]
    #L50 [Calcular a posição do carater no alfabeto]
    Onde=alfa.find(letra)
    #L60 [Escrever o carater se for letra, atualizando numero de letras]
    if Onde!=-1:
           print("Carater nº", i + 1,  letra)
#L70 [Terminar]
