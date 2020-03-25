"""
estruturas lógicas


num_11 = int(input('Digite o primeiro numero: '))
num_12 = int(input('Digite o segundo numero: '))

if num_11 > num_12:
    print(f'´O primeiro numero é o maior - {num_11}')
else:
    print(f'´O segundo numero é o maior - {num_12}')

num_2 = float(input('Digite um numero: '))

if num_2 > 0:
    print(f'´A raiz do numero é {num_2 ** (1/2)}')
else:
    print(f'´Numero invalido - {num_2}')

"""

num_5 = int(input('Digite um numero: '))

resto = num_5 % 2

if resto == 0:
    print(f'´numero par')
else:
    print(f'´numero impar')
