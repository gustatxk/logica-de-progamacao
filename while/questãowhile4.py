nota = float(input("Digite uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    print('INVÁLIDO')
    nota = float(input("Digite uma nota válida: "))
    