pessoa= {'Nome': 'Seito kaiba', 'Idade': 22, 'Profissão': 'Duelista'}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


pessoa= {'Nome': 'Seito Kaiba', 'Idade': 22, 'Profissão': 'Duelista'}
print(pessoa["Nome"])

for chaves in pessoa:
    print(chaves)