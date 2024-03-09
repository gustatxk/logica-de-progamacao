countv = 0
countc = 0
vogais = ['a','e','i','o','u']
vogal = []
cons = []
print("Consoantes ou vogais!")
print("_"*20)
for l in range(1,11):
    lgd = str(input("Digite uma letra: ").lower())
    print("_"*20)
    if lgd in vogais:
        vogal.append(lgd)
        countv += 1
    else:
        cons.append(lgd)
        countc += 1


print(f"Total de vogais: {countv}")
print(vogal)
print(f"Total de consoantes: {countc}")
print(cons)



