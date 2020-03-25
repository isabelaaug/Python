"""
Dictionary Comprehension

Sintaxe:

list Comprehension --- {alor for valor in iterável}
dictinary Comprehension --- {chave: valor for valor in iterável}

Ex:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

----------------

obs: se tiver elementos repetidos, eles serão ignorados
numeros = [1, 2, 3, 4, 5] ou (1, 2, 3, 4, 5) ou {1, 2, 3, 4, 5}
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

----------------
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mix)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
---------------
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)  # {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

"""




