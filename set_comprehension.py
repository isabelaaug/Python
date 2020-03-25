"""
Set Comprehension - CONJUNTOS (SEM VALORES REPETIDOS)





"""
numeros = {num for num in range(1, 7)}
print(numeros)  # {1, 2, 3, 4, 5, 6}

numeros = {x ** 2 for x in range(10)}
print(numeros)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

numeros = {x: x for x in range(10)}  # transforma um cojunto em dicionário
print(numeros)  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

letras = {letra for letra in 'isabela augusta'}
print(letras)  # {'u', 'l', 'i', ' ', 'g', 'b', 'a', 't', 's', 'e'}
