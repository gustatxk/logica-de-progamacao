#inicia um loop infinito
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
        print("Fechando...")
        break


