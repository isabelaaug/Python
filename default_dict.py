"""
Collections Default Dict
https://docs.python.org/3/library/collections.html

dicio = {'curso': 'python'}
print(dicio['curso'])
print(dicio['outro'])  # key error

-permite por meio de um lambda criar um valor default para caso a chave não tenha um valor definido
e caso a chave não exista ela será criada também com o valor default atribuido
-lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'python'
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])
print(dicionario)
