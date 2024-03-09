def continua():
    opcao = int(input('''\tDejesa continua?
        [1] Para sim
        [2] Para não'''))
    if opcao == 1:
        continue
    elif opcao == 2:
        break

        
def dados():
    print("-=-"*10)
    nome = str(input("Digite seu nome: ")).capitalize()
    idade = int(input("Digite sua idade: "))
    print("-=-"*10)
    print(f"nome: {nome}")
    if idade is None:
        print("Idade não informada!")
    else:
        print(f"Idade: {idade}")
while True:
    dados()
    continua()