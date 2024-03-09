f = 1
num = int(input("digite um número: "))
if num < 0:
    print("não é possível calcular o fatorial de um número negativo")
elif num == 0:
    print("0! é igual a 1")
elif num == 1:
    print("1! é igual a 1")
else:
    for i in range(num, 1, -1):
        f = f*i
    print(f)