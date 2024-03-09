times = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cuiabá', 'São paulo', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco da gama', 'Cruzeiro', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')
opcao= int(input("Digite a posição da tabela que deseja consultar: "))
while opcao<1 or opcao>20:
    print("Posição inválida! Digite um número de 1 a 20")
    opcao= int(input("Digite a posição da tabela que deseja consultar: "))
print(f"{times[opcao-1]} está na {opcao }° posição")