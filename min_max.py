"""
Min e Max

max()  -- mostra o maior valor, seja em lista, tupla, set e dicionarios

numeros = [6, 8, 9, 15, 2, 3, 1]
print(max(numeros))  # 15
dic = {'a': 6, 'b': 8, 'c': 9, 'd': 15, 'e': 2, 'f': 3, 'g': 1}
print(max(dic))  # g
dic = {'a': 6, 'b': 8, 'c': 9, 'd': 15, 'e': 2, 'f': 3, 'g': 1}
print(max(dic.values()))  # 15
print(max(3, 43))  # 43

------------------------------

v1 = int(input('informe um valor: '))
v2 = int(input('informe outro valor: '))
print(f'o maior valor eh o {max(v1, v2)}')

--------------------

print(max('a', 'gf', 'dce'))  # gf
print(max('Geek University'))  # y

-------------------------------------------------------

min() -- mostra o menor valor, seja em lista, tupla, set e dicionarios

numeros = [6, 8, 9, 15, 2, 3, 1]
print(min(numeros))  # 1
dic = {'a': 6, 'b': 8, 'c': 9, 'd': 15, 'e': 2, 'f': 3, 'g': 1}
print(min(dic))  # a
dic = {'a': 6, 'b': 8, 'c': 9, 'd': 15, 'e': 2, 'f': 3, 'g': 1}
print(min(dic.values()))  # 1
print(min(3, 43))  # 3


v1 = int(input('informe um valor: '))
v2 = int(input('informe outro valor: '))
print(f'o maior valor eh o {min(v1, v2)}')

print(min('a', 'gf', 'dce'))  # a
print(min('Geek University'))  # ' '

---------------------------------------

nomes = ['Alice', 'Samuel', 'Thomas', 'Oliveira']

print(max(nomes))  # Thomas -- considerando ordem alfabetica
print(min(nomes))  # Alice -- considerando ordem alfabetica

print(max(nomes, key=lambda nome: len(nome)))  # Oliveira -- considerando tamanho do nome
print(min(nomes, key=lambda nome: len(nome)))  # Alice -- considerando tamanho do nome

-------------------------------------


"""

musicas = [
    {'titulo': 'quarta cadeira', 'tocou': 8},
    {'titulo': 'beija flor', 'tocou': 2},
    {'titulo': 'paradinha', 'tocou': 15},
    {'titulo': 'menina solta', 'tocou': 5}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

maximo = 0
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']
for musica in musicas:
    if musica['tocou'] == maximo:
        print(musica['titulo'])

minimo = 9999
for musica in musicas:
    if musica['tocou'] < minimo:
        minimo = musica['tocou']
for musica in musicas:
    if musica['tocou'] == minimo:
        print(musica['titulo'])
