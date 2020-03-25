"""
List Comprehension

-gera uma nova lista com dados processodos a partir de outro iterável

numeros = [1, 5, 6, 4]
res = [numero * 10 for numero in numeros]
print(res)  # [10, 50, 60, 40]
res = [numero / 10 for numero in numeros]
print(res)  # [0.1, 0.5, 0.6, 0.4]


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)  # [1, 25, 36, 16]

------------------------------------
# Loop  x  List Comprehension

# Loop
numeros = [1, 5, 6, 4]
numero_dobrado = []

for numero in numeros:
    numeros_dobrados = numero * 2
    numero_dobrado.append(numeros_dobrados)

print(numero_dobrado)  # [2, 10, 12, 8]


# List Comprehension
print([numero * 2 for numero in numeros])  # [2, 10, 12, 8]

----------------------------------------------
nome = 'isabela'

print([letra.upper() for letra in nome])  # ['I', 'S', 'A', 'B', 'E', 'L', 'A']

amigos = ['maria', 'joao', 'pedro', 'caio']


def maiusculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


print([amigo[0].upper() for amigo in amigos])  # ['M', 'J', 'P', 'C']
print([amigo.title() for amigo in amigos])  # ['Maria', 'Joao', 'Pedro', 'Caio']
print([maiusculo(amigo) for amigo in amigos])  # ['Maria', 'Joao', 'Pedro', 'Caio']

print([numero * 3 for numero in range(1, 11)])  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])  # [False, False, False, True, True, True]
print([str(numero) for numero in [1, 2, 3, 4, 5]])  # ['1', '2', '3', '4', '5']

-------------------------------
numeros = [1, 5, 6, 4]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)  # [6, 4]
print(impares)  # [1, 5]
# qualquer número par módulo de 2 é 0, no caso, False e not False = True
pares = [numero for numero in numeros if not numero % 2]
# qualquer número impar módulo de 2 é 1, no caso, True
impares = [numero for numero in numeros if numero % 2]
print(pares)  # [6, 4]
print(impares)  # [1, 5]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)  # [0.5, 2.5, 12, 8]

"""

