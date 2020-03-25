"""
Ordered Dict
-em um dicionario, a ordem de inserção, não é garantida.

paises = {'br': 'brasil', 'py': 'paraguai', 'eua': 'estados unidos', 'arg': 'argentina'}
print(paises)

dicionario = OrderedDict({'br': 'brasil', 'py': 'paraguai', 'eua': 'estados unidos', 'arg': 'argentina'})

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

dicio1 = {'a': 1, 'b': 2}
dicio2 = {'b': 2, 'a': 1}

print(dicio1 == dicio2)  # True, pois m dicionários comuns a ordem não importa

dicio3 = OrderedDict({'a': 1, 'b': 2})
dicio4 = OrderedDict({'b': 2, 'a': 1})

print(dicio3 == dicio4)  # False, pois a ordem dos elementos é diferente

"""
from collections import OrderedDict


