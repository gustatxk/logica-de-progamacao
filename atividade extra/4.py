# Inicia um loop infinito
while True:
    # Exibe o menu de opções
    print("Menu de médias:")
    print("1 Calcular a Média Aritmética")
    print("2 Calcular a Média Ponderada")
    print("3 Sair do programa")
    
    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Se a opção for 1 o programa solicita a quantidade de notas
        quantn = int(input("Quantas notas deseja inserir: "))
        s = 0
        for i in range(quantn):
            n = float(input(f"Insira a nota {i + 1}: "))
            s += n
        # Calcula a média aritmética e a exibe
        mediaari = s / quantn
        print(f"A média aritmética é: {mediaari}")
    elif opcao == "2":
        # Se a opção for 2 o programa solicita a quantidade de notas e pesos
        quantn = int(input("Quantas notas deseja inserir: "))
        soman = 0
        somap = 0
        for i in range(quantn):
            n = float(input(f"Insira a nota {i + 1}: "))
            p = float(input(f"Insira o peso da nota {i + 1}: "))
            soman += n * p
            somap += p
        # Calcula a média ponderada e a exibe
        mediapon = soman / somap
        print(f"A média ponderada é: {mediapon}")
    elif opcao == "3":
        # Se o usuário escolher sair encerra o programa
        print("Programa encerrado")
        break
    else:
        # Se o usuário inserir uma opção inválida exibe uma mensagem de erro
        print("Opção inválida, digite novamente")
    opcao = int(input('''Desejar continua? 
    [1] Para sim
    [2] Para não
    ''')) #saber se o usuário que continuar
    if opcao == 2:
        print("Programa encerrado!")
        break
