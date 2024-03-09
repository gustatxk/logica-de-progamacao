minimo = []
for i in range(1,11):
    num = int(input(f"digite o {i}° número: "))
    minimo.append(num)
print(f"O menor valor inserido foi: {min(minimo)}")
