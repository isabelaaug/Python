"""
Erros mais comuns

https://docs.python.org/3/library/exceptions.html

- ler as saidas de erros geradas

--SyntaxError: escrever incorretamente ou utilizar uma palavra reservada do sistema

def funcao:
    print('isabela')  # SyntaxError: invalid syntax

def = 3  # SyntaxError: invalid syntax

-------------------------------------

--NameError: quando a função ou variavel não é definida

isa()  # NameError: name 'isa' is not defined

---------------------------------------

--TypeError: quando funcao/operação/ação é aplicado a um tipo errado.

print('Geek' + 3)  # TypeError: can only concatenate str (not "int") to str

-------------------------------------

--IndexError:qundo se acessa um indice invalido em uma lista

lista = ['isabela']
print(lista[2])  # IndexError: list index out of range

-------------------------------------

--ValueError: atribuir um valor inapropriado à uma função

print(int('Str'))  # ValueError: invalid literal for int() with base 10: 'Str'

------------------------------------------

--KeyError: acessar um dicionário com uma chave invalida

dic = {'a': 3}
print(dic['b'])  # KeyError: 'b'

----------------------------------------

--AttributeError: quando uma variavel não tem um atributo/função

tupla = (11, 2, 3)
tupla.sort()
print(tupla)  # AttributeError: 'tuple' object has no attribute 'sort'

--------------------------------------------

--IndentationError: quando a identação de 4 espaços não é respeitada

def nova():
print('oi')  # IndentationError: expected an indented block

"""






