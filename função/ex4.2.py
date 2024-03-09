def continua():
    while True:
        opcao = int(input('''\tDejesa continuar?
        [1] Para sim
        [2] Para não\n'''))
        if opcao == 1:
            continue
        elif opcao == 2:
            break
        else:
            print("Opção inválida. Por favor, escolha 1 para sim ou 2 para não.")

def dados():
    print("-=-"*10)
    nome = str(input("Digite seu nome: ")).capitalize()
    idade = int(input("Digite sua idade: "))
    print("-=-"*10)
    print(f"Nome: {nome}")
    if idade is None:
        print("Idade não informada!")
    else:
        print(f"Idade: {idade}")

while True:
    dados()
    continua()