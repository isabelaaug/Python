"""
Tuplas

1. representada por () e definicadas pela virgula
2. são imutaveis, todas as operações com elas, gera uma nova tupla, não permitindo adição e remoção
3. isso não existe:  tupla = (4)
4. utilizar listas que não podem ser modificadas (ex. meses, chaves de dicionários)

- são mais rapidas que listas
- deixam o código mais seguro



tupla1 = 1, 2, 3, 4
tupla2 = (1, 2, 3, 4)
tupla3 = (4,)
tupla4 = 4,
tupla5 = tuple(range(11))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla6 = ('isabela augusta', 'de oliveira')

# desempacotamento de tupla
tupla6 = ('isabela augusta', 'de oliveira')
nome, sobrenome = tupla6
print(nome)
print(sobrenome)

print(sum(tupla1))  # soma -- se todos inteiros
print(max(tupla1))  # max valor -- se todos inteiros
print(min(tupla1))  # min valor -- se todos inteiros
print(len(tupla1))  # tamanho da lista

# concatenação de tuplas
tupla1 = (1, 2, 3, 4)
print(tupla1)  # (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)
print(tupla2)  # (5, 6, 7, 8
tupla3 = tupla1 + tupla2  # (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla1 + tupla2)  # (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla1)  # (1, 2, 3, 4)
print(tupla2)  # (5, 6, 7, 8)
print(tupla3)  # (1, 2, 3, 4, 5, 6, 7, 8)

# encontrar elemento
tupla1 = (1, 2, 3, 4)
print(3 in tupla1)  # true or false

# iterando
tupla1 = (1, 2, 3, 4)
for n in tupla1:
    print(n)
for indice, valor in enumerate(tupla1):
    print(indice, valor)

tupla1 = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
i = 0
while i < len(tupla1):
    print(tupla1[i])
    i = i + 1



# contando elementos
tupla1 = (1, 4, 3, 4)
tupla2 = ('i', 'a')
tupla3 = ('isabela augusta', 'de oliveira')
novo = tuple('isabela augusta')
print(tupla2.count('a'))
print(tupla1.count(4))
print(novo)
print(novo.count('a'))

# descobrir indice
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses.index('mai'))

# copiando tuplas -- não ocorrendo shallow copy
tupla1 = (1, 4, 3, 4)
print(tupla1)
nova = tupla1
print(nova)
outra = tupla1 + nova
print(outra)
print(nova)
print(tupla1)

"""


