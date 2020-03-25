"""
Conjuntos
-são chamados de sets e não possuem valores duplicados e ordenados
-elementos não são indexados(acessados via indice)
-úteis quando precisamos armazenar elementos sem se importar com ordenação
ou não se preocurar com chaves, valores e itens duplicados
-são referenciados com {}
-class set

Diferenças entre conjuntos e dicionarios:
-conjunto tem valor  x  dicionários chave: valor

# definindo um conjunto
conjunto = set({1, 5, 3, 2, 5, 1, 7, 6})
print(conjunto)  # {1, 2, 3, 5, 6, 7} não repete valores
print(type(conjunto))
conjunto = set({'isabela oliveira'})
print(conjunto)  # {'isabela oliveira'}
print(type(conjunto))
conjunto = set('isabela oliveira')
print(conjunto)  # {'a', ' ', 'b', 'r', 'i', 's', 'e', 'v', 'o', 'l'} não repete valores
print(type(conjunto))
tupla = (1, 5, 3, 2, 5, 1, 7, 6)
conjunto = set(tupla)
print(conjunto)  # {1, 2, 3, 5, 6, 7} não repete valores
print(type(conjunto))
conjunto = {1, 5, 3, 2, 5, 1, 7, 6}
print(conjunto)  # {1, 2, 3, 5, 6, 7} não repete valores
print(type(conjunto))
conjunto = {1, 5, 3, 2, 5, 1, 7, 6}

if 9 in conjunto:
    print('achei')
else:
    print('não achei')

# aceitam elementos duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')
# aceitam elementos duplicados
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')
# não aceitam chaves duplicadas
dicio = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dicio')
print(f'Dicionário: {dicio} com {len(dicio)} elementos')
# não aceitam elementos duplicados
conjunto = set({99, 2, 34, 23, 2, 12, 1, 44, 5, 34})
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

conjunto = {1, 'a', True, 2.54}
print(conjunto)  # {1, 2.54, 'a'}

for valor in conjunto:
    print(valor)  # 1, 2.54, 'a'

cidades = ['Curitiba', 'São Paulo', 'Joinville', 'Cuiaba', 'Curitiba', 'Joinville']
print(cidades)
print(f'Total de pessoas {len(cidades)}')
print(f'Total de cidades {len(set(cidades))}')

# adicionando elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
conjunto.add(541)  # {1, 2, 99, 34, 5, 12, 44, 23, 541}
conjunto.add(99)  # não adiciona, pois já existe, mas também não gera erro
print(conjunto)

# remover elementos

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}

conjunto.remove(99)  # {1, 2, 34, 5, 12, 44, 23}
conjunto.remove(54)  # keyerror
print(conjunto)

conjunto.discard(34)
print(conjunto)  # {1, 2, 5, 12, 44, 23}

# copiando conjuntos
# deep copy
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
novo = conjunto.copy()
print(novo)
novo.add(28)
print(conjunto)
print(novo)

# shallow copy
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
novo = conjunto
print(novo)
novo.add(28)
print(conjunto)
print(novo)

# zerar conjunto
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(conjunto)
conjunto.clear()
print(conjunto)

# métodos matematico
alunos_python = {'pedro', 'joão', 'lucas', 'miguel', 'arthur', 'gustavo'}
alunos_c = {'fernando', 'ana', 'rafael', 'pedro', 'lucas'}

# junta todos os elementos sem gerar repetições
unicos1 = alunos_python.union(alunos_c)
print(unicos1)
unicos2 = alunos_python | alunos_c
print(unicos2)

# junta os elementos em comum nos dois conjuntos
ambos1 = alunos_python.intersection(alunos_c)
print(ambos1)
ambos2 = alunos_python & alunos_c
print(ambos2)

# junta os elementos que não se repetem nos dois conjuntos
so_python = alunos_python.difference(alunos_c)
print(so_python)
so_c = alunos_c.difference(alunos_python)
print(so_c)

# soma, valor máximo e valor minimo se os valores forem todos inteiros
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
# tamanho
print(len(conjunto))

"""




