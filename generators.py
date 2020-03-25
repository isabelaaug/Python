"""
Generators -- Tuple comprehension

nomes = ['Carla', 'Caio', 'Camila', 'Cristiano']
res = list((nome[0] == 'C' for nome in nomes))  # [True, True, True, True]
print(res)

----------------------------

# retorna a quantidade de bytes em memoria do parametro
from sys import getsizeof

print(getsizeof('isa'))
print(getsizeof('isabela'))
print(getsizeof(99))
print(getsizeof(2))
print(getsizeof(165453156))
print(getsizeof(True))

------------------------------------

# gerando uma lista de numeros com uma list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista de numeros com uma set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista de numeros com uma dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# gerando uma lista de numeros com generator
res = list(x * 10 for x in range(1000))
print(res)
print(getsizeof(res))
gen = getsizeof(x * 10 for x in range(1000))

print(f'List comprehension: {list_comp}')
print(f'Set comprehension: {set_comp}')
print(f'Dict comprehension: {dict_comp}')
print(f'Genarator ou tuple comprehension: {gen}')

---------------------------------------


# iterar
gen = (x * 10 for x in range(1000))

for num in gen:
    print(num)

"""

from sys import getsizeof






