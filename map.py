"""
Map
-mapeamento de valores para função

import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))

raios = [2, 3, 5, 0.5]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Usando Map

areas = map(area, raios)
print(list(areas))

# Usando Map com lambda, mas após utilizar o resultado uma vez, ele zera.

a = map(lambda raio: math.pi * (raio ** 2), raios)
print(list(a))  # [12.566370614359172, 28.274333882308138, 78.53981633974483, 0.7853981633974483]
print(list(a))  # []

---------------------------------

cidades = [('Berlim', 29), ('Tokio', 15), ('Nova York', 24), ('Londres', 9), ('Bueno Aires', 27)]

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))  # [('Berlim', 84.2), ('Tokio', 59.0), ('Nova York', 75.2)...]

"""


