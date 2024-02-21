print("Qual a temperatura?")
temp = int(input())

if temp < 5:
    print("Muito frio")
elif temp < 10:
    print("Frio")
elif temp < 20:
    print("Ameno")
elif temp < 30:
    print("Quente")
else:
    print("Muito quente")