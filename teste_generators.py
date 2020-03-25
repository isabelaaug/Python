"""
Teste de memoria Generators

# funcao usando lista
def fibo(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fibo(100000):  # 469 mb
    print(n)

# funcao usando geradores
def fibo(max):
    contador, a, b = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fibo(100000):  # 3 mb
    print(n)

------------------------------

def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()  # generator object
print(ge1)

ge2 = (num for num in range(1, 10))
print(ge2)  # generator expression

print(next(ge2))



"""
import time

gen_inicio = time.time()
print(sum(num for num in range(1000000000)))
gen_tempo = time.time() - gen_inicio

list_inicio = time.time()
print(sum(num for num in range(1000000000)))
list_tempo = time.time() - list_inicio


print(f'Generator {gen_tempo}')
print(f'List Comprehension {list_tempo}')