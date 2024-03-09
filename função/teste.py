soma = 0
lista = []
def temp():
    for i in range(0,7):
        dia_da_semana = float(input(f"Digite a temperatura do {i + 1}º dia da semana: "))
        soma = dia_da_semana
        operacao = soma + dia_da_semana
        lista.append(dia_da_semana)
    soma = operacao / 7
    print(f'A média da temperatura da semana é {soma:.2f}')
    print(f"A temperatura máxima da semana foi {max(lista)}")
    print(f"A temperatura mínima da semana foi {min(lista)}")
temp()
    