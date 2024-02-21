print("Qual o valor de a?: ")
a = int(input())
print("Qual o valor de b?: ")
b = int(input())
while b < a:
    print("Qual o valor de b?: ")
    b = int(input())
print("Qual o valor de c?: ")
c = int(input())
print("Qual o valor de d?: ")
d = int(input())
while d < c:
    print("Qual o valor de d?: ")
    d = int(input())
for x in range(a, b, 2):
    for y in range (c, d, 4):
        if y == -3 or x == 2:
            fxy = x ** 3 + y ** 2
        else:
            fxy = (4*x**2-5*x+8) / ((y+3) * (x-2))
    print("f (",x, ",", y, ")=", fxy)
