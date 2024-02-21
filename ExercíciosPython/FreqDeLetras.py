alfa = "abcdefghijklmnopqrstuvwxyz"
freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

texto = input("Texto? ")
while texto == "":
    texto = input("Texto? ")

for l in range(len(texto)):
    car = texto[l]
    onde = alfa.find(car)

    if onde != -1:
        freq[onde] = freq[onde] + 1

for i in range(25):
    if freq[i] > 0:
        print(alfa[i], "ocorre", freq[i], "vezes")