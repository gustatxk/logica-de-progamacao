print("\tVerificador de Senha")
nome = str(input("Digite seu nome: "))
senha = str(input("Digite sua senha: "))
while nome == senha:
    print("Senha inválida")
    senha = str(input("Digite sua senha novamente: "))  
    if senha != nome:
        print("Senha válida")
        