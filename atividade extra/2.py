#inicia um loop infinito 
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

