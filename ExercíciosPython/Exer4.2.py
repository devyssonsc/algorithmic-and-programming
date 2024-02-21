f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a = int(input("Qual o limite superior?"))
while a <= 0:
 a = int(input("Qual o limite superior"))
soma=0
print("\n****")
for x in range(-a, a+1):
    if x <0:
        f[x+a] = abs(x)
    elif x == 0:
        f[x+a] = 0
    else:
        f[x+a]=1
        for y in range(x,1,-1):
            f[x+a]= f[x+a] * y
    soma=soma+f[x+a]
    print("F(", x, ")=", f[x+a])
media=soma/(2*a+1)
print("\nMedia=",round(media,2))
for x in range(a,-a-1,-1):
    if f[x+a] > media:
        print("F(", x, ")=", f[x+a],">",round(media,2))