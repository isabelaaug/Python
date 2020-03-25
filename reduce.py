"""
Reduce
- substitui um loop for
- precisa receber 2 parametros

dados = [a1, a2, a3, ..., an]

def funcao(x, y):
    return x * y

reduce(funcao, dados)

Como funciona:
    Passo 1:
    res1 = f(a1, a2)
    Passo 2:
    res2 = f(res1, a3)
    Passo 3:
    res3 = f(res2, a4)
    ...
    resn = f(resn, an)


"""

from functools import reduce

dados = [2, 6, 8, 5, 4, 4, 9, 15]

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)  # 1036800

res = 1

for valor in dados:
    res = res * valor

print(res)  # 1036800
