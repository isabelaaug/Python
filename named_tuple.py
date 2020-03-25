"""
Named Tuple

-é uma tupla que podemos especificar nome e parametros

"""
from collections import namedtuple

dog1 = namedtuple('cachorro', 'idade raca nome')
dog2 = namedtuple('cachorro', 'idade, raca, nome')
dog3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

barack = dog3(idade=3, raca='SRD', nome='Barack')
print(barack)
print(barack[0])
print(barack[1])
print(barack[2])

print(barack.idade)
print(barack.raca)
print(barack.nome)

print(barack.index('SRD'))  # indice
print(barack.count('SRD'))  # repetição
