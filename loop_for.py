"""
loop for

nome = 'isabela augusta'
lista = [1, 3, 5, 4]
numeros = range(1, 10)

enumerate((0, 'i'), (1, 's'),...)

for valor, letra in enumerate(nome):
    print(valor)

-------------------

for letra in nome:  # iterando em uma string
    print(letra)
for letra in nome:  # iterando em uma string na mesma linha
    print(letra, end='')

------------------------------

for numero in lista:  # iterando em uma lista
    print(numero)

------------------------

for numeros_range in numeros:  # iterando em uma range 1 à 9 (valor final -1)
    print(numeros_range)

for indice, letra in enumerate(nome):
    print(nome[indice])
for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome): -- o underline significa que descartamos o valor
    print(letra)
for valor, letra in enumerate(nome):
    print(valor)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
for valor in enumerate(nome):
    print(valor)
(0, 'i')
(1, 's')
(2, 'a')
(3, 'b')
(4, 'e')
(5, 'l')
(6, 'a')
(7, ' ')
(8, 'a')
(9, 'u')
(10, 'g')
(11, 'u')
(12, 's')
(13, 't')
(14, 'a')

qntd = int(input('Quantas vezes ele deve rodar?'))
for n in range(1, qntd+1):
    print(f'Imprimindo {n}')

qntd = int(input('Quantas vezes ele deve rodar? '))
soma = 0

for n in range(1, qntd+1):
    num = int(input(f'Informe o valor {n}/{qntd}: '))
    soma = soma + num

print(f'A soma é {soma}')

nome = 'isabela'
nome + ' augusta'  # concatenando no terminal

BREAK

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')


    


"""

lista = []
cont = 0
qtd = int(input('quantos numeros voce deseja digitar ? : '))
for c in range(qtd):
    num = int(input('digite um numero : '))
    lista.append(num)

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')





"""
adicionando emojis https://apps.timwhitlock.info/emoji/tables/unicode

# Original U+1F60D
# modificado U0001F60D
for _ in range(4):
    for numero in range(1, 11):
        print('\U0001F60D' * numero)
"""