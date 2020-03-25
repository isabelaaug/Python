"""
Len, abs, sum e round

len() -- retorna o numero de itens de um iterável

print(len('Isabela Augusta'))  # 15
==
print('Isabela Augusta'.__len__())  # 15

----------------------------------------

abs() -- valor absoluto de um inteiro. Valor real sem sinal

print(abs(-5))  # 5
print(abs(5))  # 5
print(abs(-5.14))  # 5.14
print(abs(5.14))  # 5.14

----------------------------------------------------

sum() -- podendo receber um valor inicial (defalt zero), retorna a soma de todos os elementos

print(sum([1, 2, 5, 8, 7, 4]))  # 27
print(sum([1, 2, 5, 8, 7, 4], 5))  # 5 como valor inicial -- 32
print(sum({'a': 1, 'b': 2}.values()))  # 2

------------------------------------------------

round() -- retorna o numero arredondado para n casas decimais

print(round(12.4))  # 12
print(round(12.5))  # 12
print(round(12.9))  # 13
print(round(12.8))  # 13
print(round(12.1))  # 12
print(round(12.4464548, 2))  # 12.45 indicando o numero de casas decimais
print(round(12.845, 2))  # 12.85
print(round(12.844, 2))  # 12.84

"""






