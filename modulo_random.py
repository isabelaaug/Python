"""
Modulo random

Modulos: são arquivos python.

Random -- gera numeros aletórios

import random

# todas as funções. atributos, classes e propriedades ficam disponiveis e em memoria

print(random.random())

--------------------------------

from random import random

# importa apenas a função solicitadas

for i in range(10):
    print(random())

----------------------------------

from random import uniform

# importa apenas a função que gera valores reais entre valores estabelecidos

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluido -- 3.0067547251140563

-----------------------

from random import randint

# importa apenas a função que gera valores inteiros entre valores estabelecidos

for i in range(6):
    print(randint(1, 61), end=', ')  # 61 não é incluido

------------------------------

from random import choice

# importa apenas a função que mostra um valor entre um iteravel

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice('isabela augusta'))

"""

from random import shuffle

# importa apenas a função que embaralha dados

jogadas = ['k', 'q', 'j', 'a', '2']

print(jogadas)  # ['k', 'q', 'j', 'a', '2']
shuffle(jogadas)  # ['k', '2', 'j', 'q', 'a']
print(jogadas)

print(jogadas)
shuffle(jogadas)
print(jogadas[0])



