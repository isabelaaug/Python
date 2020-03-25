"""
Mapas

receita = {'jan': 5624, 'fev': 4524, 'mar': 5000, 'abr': 9000, 'mai': 5624}
print(receita)
print(receita.keys())  # dict_keys(['jan', 'fev', 'mar', 'abr', 'mai'])
print(receita.values())  # dict_values([5624, 4524, 5000, 9000, 5624])

# interar sobre dicionários
for chave in receita:
    print(chave)  # jan

for chave in receita:
    print(receita[chave])  # 5624

for chave in receita:
    print(f'{chave} : {receita[chave]}')  # jan : 5624

for chave in receita.keys():
    print(receita[chave])  # 5624

for valor in receita.values():
    print(valor)  # 5624

# desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# soma, valor máximo e valor minimo se os valores forem todos inteiros
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
# tamanho
print(len(receita))


"""
receita = {'jan': 5624, 'fev': 4524, 'mar': 5000, 'abr': 9000, 'mai': 4820}
print(receita)


