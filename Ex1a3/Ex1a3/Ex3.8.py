a = int(input("Qual o limite inferior?"))
while a <= 0:
    a = int(input("Qual o limite inferior?"))
b = int(input("Qual o limite superior?"))
while b < a:
    b = int(input("Qual o limite inferior?"))
print("\n****")
for x in range(a, b + 1):
    if x > 9:
        fx = 2 * x
    else:
        fx = x ** 2
    print("F(", x, ")=", fx)