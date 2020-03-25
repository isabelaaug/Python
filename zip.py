"""
Zip

zip() -- só é possivel utilizar o resultado uma vez
- ignora elementos que não formam pares

lista1 = [5, 2, 3, 1, 7]
lista2 = [6, 8, 9, 15, 30]

zip1 = list(zip(lista1, lista2))
print(zip1)  # [(5, 6), (2, 8), (3, 9), (1, 15)]
zip2 = list(zip(lista1, lista2, 'isabe'))
print(zip2)  # [(5, 6, 'i'), (2, 8, 's'), (3, 9, 'a'), (1, 15, 'b'), (7, 30, 'e')]

tupla = 5, 95, 41
lista = [6, 4, 74]
dic = {'a': 1, 'b': 2, 'c': 28}
zt = zip(tupla, lista, dic)  # [(5, 6, 'a'), (95, 4, 'b'), (41, 74, 'c')]
print(list(zt))
zt = zip(tupla, lista, dic.values())  # [(5, 6, 1), (95, 4, 2), (41, 74, 28)]
print(list(zt))

dados = [(2, 4), (5, 7), (8, 2)]
print(list(zip(*dados)))  # [(2, 5, 8), (4, 7, 2)]

--------------------------------

prova1 = [5, 9, 3, 21]
prova2 = [6, 8, 9, 15]
alunos = ['maria', 'joao', 'caio', 'lucas']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)  # {'maria': 6, 'joao': 9, 'caio': 9, 'lucas': 21}

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))  # {'maria': 6, 'joao': 9, 'caio': 9, 'lucas': 21}

"""



