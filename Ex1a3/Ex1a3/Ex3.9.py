a = int(input("Qual o limite inferior?"))
while a <= 0:
    a = int(input("Qual o limite inferior?"))
b = int(input("Qual o limite superior?"))
while b < a:
    b = int(input("Qual o limite inferior?"))
print("\n****")
for x in range (a,b+1):
    for y in range (2,5):
        if x > 9:
            fxy = 2 * x - y
        else:
            fxy = (x - y) ** 2
        print("F(", x, ",", y, ")=", fxy)