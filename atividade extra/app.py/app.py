while True:
    print("Menu de opcões:")
    print("1 Calculadora de IMC")
    print("2 Conversor de moedas")
    print('3 Tabuada')
    print("4 Calcular média")
    print("5 Conversor de medida de comprimento")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        while True:
            altura = float(input("Digite sua altura em metros: "))
            while altura < 0 or altura > 3: #definir os limites da altura 
                print("altura inválida!")
                altura = float(input("Digite sua altura em metros novamente: "))
            peso = float(input("Digite seu peso em kg: "))
            while peso < 0 or peso > 595: #definir os limites de peso
                print("Peso inválido!")
                peso = float(input("Digite seu peso em kg novamente: "))
            print('Agora iremos calcular seu IMC')
            print('o IMC é calculado da seguinte forma IMC = peso (kg) / altura (m)2')
            IMC = peso / altura**2 #cálculo do IMC
            if IMC < 18.5: #especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está abaixo do peso!")
            elif 18.5 <= IMC <= 24.9: #especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está com um peso saudável!")
            elif 25.0 <= IMC <= 29.9: #especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está com sobrepeso!")
            elif 30.0 <= IMC <= 34.9:#especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está com obesidade grau 1!")
            elif 35.0 <= IMC <= 39.9:#especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está com obesidade grau 2!")
            elif IMC >= 40.0:#especificação do IMC
                print(f"Seu IMC é {IMC:.2f} e você está com obesidade grau 3! (mórbida)")
            opcao = int(input('''Desejar continua? 
            [1] Para sim
            [2] Para não
            ''')) #saber se o usuário que continuar
            if opcao == 2:
                print("Programa encerrado!")
                break
    elif opcao == 2:
        while True:
            print('''Menu de conversão:
        1 Converter Real para Dólar
        2 Converter Real para Euro
        3 Converter Dólar para Real
        4 Converter Euro para Real
        5 Sair do programa''')
            op = int(input("Digite a conversão desejada: "))
            if op  == 1: #condição para as opções 
                real = float(input("Quantos Reais você deseja converter para Dólar: R$ "))
                dolar = real/4.99 #cálculo do real para dólar
                print(f"Ao converter R$ {real} para Dólar você terá US$ {dolar}")
            elif op == 2:#condição para as opções 
                real = float(input("Quantos Reais você deseja converter para Euro: R$ "))
                euro = real/5.28 #cálculo do real para Euro 
                print(f"Ao converter R$ {real} para Euro você terá € {euro}")
            elif op == 3:#condição para as opções 
                dolar= float(input("Quantos Dólares você deseja converter para Real: US$ "))
                real = dolar/0.20 #cálculo do dólar para real 
                print(f"Ao converter US$ {dolar} para Real você terá R$ {real}")
            elif op == 4:#condição para as opções 
                euro= float(input("Quantos Euros você deseja converter para Real: €  "))
                real = euro/0.19 #cálculo do euro para real
                print(f"Ao converter € {euro} para Real você terá R$ {real}")
            elif op == 5:#condição para as opções 
                print("Programa encerrado...")
                break
            opcao = int(input('''Desejar continua? 
            [1] Para sim
            [2] Para não
            ''')) #saber se o usuário que continuar
            if opcao == 2:
                print("Programa encerrado!")
                break
    elif opcao == 3:
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
    elif opcao == 4:
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
                print("Programa encerrado!")
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
    elif opcao == 5:
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
    else:
        print("Número inválido digite novamente!") 
             