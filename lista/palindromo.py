palavra=input("Digite uma palavra: ")
lista=list(palavra.lower())
print(lista)
print(lista[::-1])
if lista == lista[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")