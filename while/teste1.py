
while True:
    print("1 Média aritmética")
    print("2 Média Ponderada")
    print("3 Sair do progama")
    if opção == '1':
        num = int(input("Digite quantas notas vai calcular"))
        s = 0
        for i in range(num):
            nota = float(input("Digite sua nota: "))
            s += nota
            media = s / num
            print(media)