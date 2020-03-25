"""
Geradores

- Sao iterators
- podem ser criados com funcoes geradoras e expressoes geradoras

funcoes x funcoes geradoras

funcoes: utilizam return apenas uma vez

funcoes geradoras: utilizam yield varias vezes


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('outro')

gen = conta_ate(6)
print(next(gen))

for num in gen:
    print(num)

print('outro')

gen = list(conta_ate(10))
print(gen)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('outro')

gen = conta_ate(6)
print(next(gen))

for num in gen:
    print(num)

print('outro')

gen = list(conta_ate(10))
print(gen)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
