"""
Lista Alinhadas

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3x3
print(listas)
print(listas[1][2])  # acessando elementos (linha e coluna) -- 6

# Loop com listas alinhadas
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(valor) for valor in lista] for lista in listas]

# gerando uma matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

velha = [['x' if numero % 2 == 0 else 'o' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)  # [['o', 'x', 'o'], ['o', 'x', 'o'], ['o', 'x', 'o']]

vazio = [['*' for i in range(1, 4)] for j in range(1, 4)]
print(vazio)  # [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

"""

