"""
Reversed

- inverte o iteravel


"""

lista = [1, 2, 5, 8, 7, 4]
print(list(reversed(lista)))  # [4, 7, 8, 5, 2, 1]
print(tuple(reversed(lista)))  # (4, 7, 8, 5, 2, 1)
print(set(reversed(lista)))  # {1, 2, 4, 5, 7, 8} não temos como definir ordem de um conjunto

for letra in reversed('Isabela Augusta'):
    print(letra, end='')  # end para escrever tudo na mesma linha -- atsuguA alebasI

print(' ')

print(''.join(list(reversed('Isabela Augusta'))))  # join junta uma lista de caracteres em uma string -- atsuguA alebasI
print('Isabela Augusta'[::-1])

for n in reversed(range(0, 11)):
    print(n)

for n in range(10, -1, -1):
    print(n)

