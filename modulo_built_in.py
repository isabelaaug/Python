"""
Modulos integrados

https://docs.python.org/3/py-modindex.html

# Alias (apelidos) para modulos e funções
import random as rdm

print(rdm.random())

-----

from random import randint as rdi, random as rdm

print(rdi(5, 9))
print(rdm())

----------------------------------------

# podemos importar todas s funçoes de um modulo utilizando o *

from random import *

print(random())

------

# podemos importar todas s funçoes de um modulo

import random

print(random.random())

--------------------------

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(2, 5))
novo = [2, 8, 4, 7]
shuffle(novo)
print(novo)
print(choice(novo))

"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(2, 5))
novo = [2, 8, 4, 7]
shuffle(novo)
print(novo)
print(choice(novo))






