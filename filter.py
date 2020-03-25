"""
Filter

-Funcao que serve para filtrar dados de uma determinada colecao
-após utilizar o resultado uma vez, ele zera.

import statistics

dados = [5.2, 5.3, 7.5, 4.8, 3.2, 6.1]

media = statistics.mean(dados)
print(f'Media: {media}')
res = filter(lambda x: x > media, dados)
print(list(res))
res = filter(lambda x: x < media, dados)
print(list(res))

---------------------------------

paises = ['Brasil', '', 'Chile', '', '', 'Argentina']
print(paises)
res = filter(None, paises)
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))

------------------------------------------
Filter  x  Map

paises = ['Brasil', '', 'Chile', '', '', 'Argentina']
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))  # ['Brasil', 'Chile', 'Argentina']
res = filter(lambda pais: pais != '', paises)
print(list(res))  # ['Brasil', 'Chile', 'Argentina']

paises = ['Brasil', '', 'Chile', '', '', 'Argentina']
res = map(lambda pais: len(pais) > 0, paises)
print(list(res))  # [True, False, True, False, False, True]
res = map(lambda pais: pais != '', paises)
print(list(res))  # [True, False, True, False, False, True]

---------------------------------------

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu acordei', 'Bate bola, jogo rapido']},
    {'username': 'lucas', 'tweets': ['Bate palma']},
    {'username': 'joao', 'tweets': []},
    {'username': 'lari', 'tweets': []},
    {'username': 'amanda', 'tweets': ['Eu sei, vc nao', 'fala mais q ta pouco', 'abre o jogo rapido']}
    ]

inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos)
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)

-----------------------------

# criar uma lista com "sua instrutora" desde que o nome tenha menos de 5 caracteres
nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))
print(lista)

"""







