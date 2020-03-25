"""
Recabendo dados do usuário
"""

# Entrada de dados
print('Qual o seu nome? ')
nome_1 = input()
print('Qual sua idade? ')
idade_1 = input()

nome_2 = input('Qual seu nome? ')
idade_2 = input('Qual sua idade? ')
idade_3 = int(input('Qual sua idade? '))


# Processamento

# Saida de dados
print('Seja bem vindx %s' % nome_1)
print('A %s tem %s anos' % (nome_1, idade_1))

print('Seja bem vindx {0}'.format(nome_1))
print('A {0} tem {1} anos'.format(nome_1, idade_1))

print(f'Seja bem vindx {nome_2}')
print(f'A {nome_2} tem {idade_2} anos')

print(f'A {nome_2} nasceu em {2018 - int(idade_2)}')
print(f'A {nome_2} nasceu em {2018 - idade_3}')