"""
Listas

# checar valor na lista
num = 18
if num in lista4:
    print('encontrei')
else:
    print('não encontrei')

# ordenar uma lista [' ', 'A', 'a', 'b', 'e', 'i', 'l', 's']
lista1.sort()
print(lista1)

# conta a repetição de informações
print(lista1.count(1))
print(lista5.count('a'))

# adicionar elementos
print(lista1)
lista1.append(51)  # apenas adiciona 1 elemento de cada vez
lista1.append([5, 5, 5])  # adiciona uma lista dentro de outra
lista1.extend([5, 5, 5])  # adiciona varios itens na lista [1, 99, 1, 4, 5, 51, [5, 5, 5], 5, 5, 5, 5, 'i', 's', 'a']
lista1.extend([5])
lista1.extend('isa')
print(lista1)

# insere na lista o valor na posição definida
lista1.insert(2, 51)
lista1.insert(2, 'isa')
print(lista1)

# insere elementos de uma lista em outra
lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista6)
print(lista1)

# inverte uma lista
lista1.reverse()
print(lista1[::-1])

# copiar uma lista
lista6 = lista4.copy()
print(lista6)

# tamanho da lista
print(len(lista1))

# remove o ultimo elemento, retornando o ultimo elemento
print(lista1)
lista1.pop()
print(lista1)

# remove elemento pelo indice 0 - ... deslocando todos os outros elemento para esquerda
print(lista1)
lista1.pop(1)
print(lista1)

# zerar a lista
print(lista1)
lista1.clear()
print(lista1)

# repetir elementos da lista [1, 99, 1, 4, 5, 1, 99, 1, 4, 5, 1, 99, 1, 4, 5]
nova = lista1 * 3
print(nova)

# converter string em lista
curso = 'prog python'
print(curso)
curso = curso.split()
print(curso)  # ['prog', 'python'] divide os elementos entre espaços

curso = 'prog,python'
print(curso)
curso = curso.split(',')
print(curso)  # ['prog', 'python'] divide os elementos entre o caracter escolhido

curso1 = ['prog', 'python']
print(curso1)
curso = ' '.join(curso1)
print(curso)  # prog python - cria uma string dividindo os elementos com espaço ou qualquer outro caracter

# iterando sobre lista

soma = 0  # soma todos os elementos da lista
for elemento in lista4:
    print(lista4)
    soma = soma + elemento
print(soma)
soma = ''  # soma todos os elementos da lista
for elemento in lista2:
    print(lista2)
    soma = soma + elemento
print(soma)

carro = []
produto = ''

while produto != 'sair':
    print('add produto até "sair": ')
    produto = input()
    if produto != 'sair':
        carro.append(produto)
for produto in carro:
    print(produto)

num1 = 1
num2 = 2
num3 = 3
          -3    -2   -1
           0     1    2
numes = [num1, num2, num3]
print(numes[1]) -- 2
print(numes[-1]) -- 3

# descobrir o indice de um item, se houver varios iguais ele mostra do primeiro
print(lista1.index(99, 1, 3)) -- 1 e 3 é o indice que ele inicia e para a busca

# indica o indice inicial
print(lista1[1:])

# indica o indice final (3-1 = [2])
print(lista1[:3])

# indica o indice inicial e final (5-1 = [4])
print(lista1[1:5])

print(sum(lista1))  # soma
print(max(lista1))  # max valor
print(min(lista1))  # min valor
print(len(lista1))  # tamanho da lista

# transformar em uma tupla
tupla = tuple(lista1)

# desempacotameto
lista = [1, 2, 3]
num1, num2, num3 = lista

# deep copy a lista copiada não é modificada se a cópia é alterada
lista = [1, 2, 3]
nova = lista.copy()
nova.append(4)
print(lista)
print(nova)

# shallow copy a alteração é feita em ambas as listas
lista = [1, 2, 3]
nova = lista
nova.append(4)
print(lista)
print(nova)

"""
lista1 = [1, 99, 1, 4, 5]
lista2 = ['i', 's', 'A', 'b', 'e', 'l', 'a', ' ']
lista3 = []
lista4 = list(range(21))
lista5 = list('isabela augusta')


