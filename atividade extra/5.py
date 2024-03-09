# Inicia um loop infinito
while True:
    #Exibe o menu de opções de conversão
    print("Menu de Conversão de Unidades de Comprimento:")
    print("1 Converter de centímetros (cm) para metros (m)")
    print("2 Converter de centímetros (cm) para quilômetros (km)")
    print("3 Converter de metros (m) para centímetros (cm)")
    print("4 Converter de metros (m) para quilômetros (km)")
    print("5 Converter de quilômetros (km) para centímetros (cm)")
    print("6 Converter de quilômetros (km) para metros (m)")
    print("7 Sair do programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        # Se a opção for 1 solicita um valor em cm
        cm = float(input("Digite o valor em centímetros (cm): "))
        m = cm / 100
        # Realiza a conversão e exibe o resultado
        print(f"{cm} cm é igual a {m} metros.")
    elif opcao == "2":
        # Se a opção for 2 solicita um valor em cm
        cm = float(input("Digite o valor em centímetros (cm): "))
        km = cm / 100000
        # Realiza a conversão e exibe o resultado
        print(f"{cm} cm é igual a {km} quilômetros")
    elif opcao == "3":
        # Se a opção for 3 solicita um valor em metros
        m = float(input("Digite o valor em metros (m): "))
        cm = m * 100
        # Realiza a conversão e exibe o resultado
        print(f"{m} metros é igual a {cm} centímetros")
    # Continua o mesmo padrão para as outras opções de conversão
    elif opcao == "4":
       m = float(input("Digite o valor em metros (m): "))
       km = m/1000
       print(f"{m} metros é igual a {km} quilômetros")
    elif opcao == "5":
        km = float(input("Digite o valor em quilômetros (km): "))
        cm = km * 100000
        print(f"{km} quilômetros é igual a {cm} centímetros")
    elif opcao == "6":
        km = float(input("Digite o valor em quilômetros (km): "))
        m = km * 1000
        print(f"{km} quilômetros é igual a {m} metros")
    elif opcao == "7":
        # Se o usuário escolher sair  encerra o programa
        print("Programa encerrado")
        break
    else:
        # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
        print("Opção inválida, digite novamente")
    opcao = int(input('''Desejar continua? 
    [1] Para sim
    [2] Para não
    ''')) #saber se o usuário que continuar
    if opcao == 2:
        print("Programa encerrado!")
        break