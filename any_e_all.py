"""
Any e All

all() -- retorna True se todos os elementos são verdadeiros ou se o iterável está vazio

Ex.:
print(all([0, 1, 2, 4]))  # False, pois o zero é false
print(all([1, 2, 4]))  # True
print(all([]))  # True
print(all((1, 2, 4)))  # True
print(all({1, 2, 4}))  # True
print(all('Isa'))  # True

nomes = ['Carla', 'Caio', 'Camila', 'Cristiano']
print(all([nome[0] == 'C' for nome in nomes]))  # True

print(all([num for num in [7, 2, 11, 6, 8] if num % 2 == 0]))

-------------------------------------

any() -- retorna True se qualquer elemento for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 4]))  # True
print(any([0, False, (), {}, '']))  # False
nomes = ['Carla', 'Caio', 'Camila', 'Cristiano']
print(all([nome[0] == 'C' for nome in nomes]))  # True
print(all([num for num in [7, 2, 11, 6, 8] if num % 2 == 0]))  # True

"""



