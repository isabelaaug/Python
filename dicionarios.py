"""
Dicionários
OBS: em algumas linguagens são conhecidos por mapas

-são coleções do tipo chave/valor
-são representados por {}
-class dict
-chaves não se repetem

# chave:valor de qualquer tipo

paises = {'br': 'brasil', 'py': 'paraguai', 'eua': 'estados unidos', 'arg': 'argentina'}
paises = dict(br='brasil', py='paraguai', eua='estados unidos', arg='argentina')
localidades = {
    (152.4455, 251.3465): 'Sao Paulo',
    (232.3243, 241.4514): 'Rio de Janeiro',
    (564.8563, 231.4171): 'Curitiba'
}


# acessando elementos
print(paises['br'])
print(paises.get('br'))

# tipos de erros ao não encontrar elementos
print(paises['bu'])  # KeyError
print(paises.get('bu'))  # None

pais = paises.get('br')
if pais:
    print(f'Encontrei o {pais}')
else:
    print('Não encotrei')

OU

pais = paises.get('br', 'não encontrado')
print(f'Encontrei o {pais}')

OU

print('br' in paises)  # True
print('paraguai' in paises)  # False
print('ru' in paises)  # False

# adicionar elementos
receita = {'jan': 1500, 'fev': 2654, 'mar': 5000}
receita['abr'] = 8000
receita['fev'] = 4524
novo1 = {'jan': 5624}
novo2 = {'mai': 5624}
receita.update(novo1)
receita.update(novo2)
num = 9000
receita['abr'] = num

# remover elementos
receita = {'jan': 5624, 'fev': 4524, 'mar': 5000, 'abr': 9000, 'mai': 5624}
retorno = receita.pop('abr')  # retorna o valor removido

del receita['fev']  # apenas remove
print(receita)

remover = 'fev'
receita = {'jan': 5624, 'fev': 4524, 'mar': 5000, 'abr': 9000, 'mai': 5624}
del receita[remover]

# listas
carrinho = []
produto1 = ['xone', 2, 900.00]
produto2 = ['gears', 1, 50.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# tuplas
produto1 = ('xone', 2, 900.00)
produto2 = ('gears', 1, 50.00)
carrinho = (produto1, produto2)
print(carrinho)
# dicionarios
carrinho = []
produto1 = {'produto': 'xone', 'quantidade': 2, 'preco': 900.00}
produto2 = {'produto': 'gears', 'quantidade': 1, 'preco': 50.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# limpar dicionarios
d = dict(a=1, b=8, c=4)
print(d)
d.clear()
print(d)

# copiando um dicionario para outro

# deep copy - original não é alterado
d = dict(a=1, b=8, c=4)
print(d)
novo = d.copy()
print(novo)
novo['d'] = 6
print(d)
print(novo)

# shallow copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)



"""
# criação de dicionarios
d1 = {}.fromkeys('a', 'b')  # chave, valor
print(d1)
d2 = {}.fromkeys(['a', 'b'], 'c')  # [chave], valor de todas as chaves
print(d2)
d3 = {}.fromkeys('teste', 'valor')  # {'t': 'valor', 'e': 'valor', 's': 'valor'}
print(d3)
d4 = {}.fromkeys(range(1, 11), 'valor')  # {'t': 'valor', 'e': 'valor', 's': 'valor'}
print(d4)



