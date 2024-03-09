# Inicia um loop infinito
while True:
    print("Escolha a operação desejada:")
    print("1 Adição")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")
    print("5 Sair do programa")
    # Solicita ao usuário que um número da operação
    opcao = input("Digite o número da operação: ")


    if opcao == "1":
        #Se a opção for 1 solicita um número de 1 a 10
        num = int(input("Digite um número de 1 a 10: "))
        if 1 <= num <= 10:
            #Realiza a adição e exibe os resultados de 1 a 10
            for i in range(1, 11):
                resultado = num + i
                print(f"{num} + {i} = {resultado}")
        else:
            # Se o número estiver fora do intervalo exibe uma mensagem de erro
            print("Número fora do intervalo válido")
    elif opcao == "2":
        #Mesma lógica para a subtração 
        num = int(input("Digite um número de 1 a 10: "))
        if 1 <= num <= 10:
            for i in range(1, 11):
                resultado = num - i
                print(f"{num} - {i} = {resultado}")
        else:
            print("Número fora do intervalo válido")
    elif opcao == '3':
        #Mesma lógica para a multiplicação 
        num = int(input("Digite um número de 1 a 10: "))
        if 1 <= num <= 10:
            for i in range(1, 11):
                resultado = num * i
                print(f"{num} * {i} = {resultado}")
        else:
            print("Número fora do intervalo válido")
    elif opcao == '4':
        # Mesma lógica para a divisão 
        num = int(input("Digite um número de 1 a 10: "))
        if 1 <= num <= 10:
            for i in range(1, 11):
                if i != 0:
                    resultado = num / i
                    print(f"{num} / {i} = {resultado}")
                else:
                    # Verifica a divisão por zero
                    print(f"Divisão por zero não é permitida.")
        else:
            print("Número fora do intervalo válido")
    elif opcao == '5':
        # Se o usuário escolher sair  encerra o programa
        print("Programa encerrado!")
        break
    else:
        #Se o usuário inserir uma opção inválida exibe uma mensagem de erro
        print("Opção inválida. Digite um número de 1 a 5 para escolher a operação")
    opcao = int(input('''Desejar continua? 
    [1] Para sim
    [2] Para não
    ''')) #saber se o usuário que continuar
    if opcao == 2:
        print("Programa encerrado!")
        break

