"""
Entendendo o *args

-parametro de entrada  --  *args == *<nome_do_parametro>
-coloca os parametros extra em uma tupla
- não aceita uma listas, pois visualiza a lista como um unico elemento. Para resolver é necessário desempacotar
a lista <nome_função>(*<nome_lista>)

def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(1))
print(soma_todos(2, 3, 6))


def nomes(nome, email, *args):
    return sum(args)


print(nomes('isa', 'gmail'))
print(nomes('isa', 'gmail', 1))
print(nomes('isa', 'gmail', 2, 3, 6))

"""


def soma_todos(*args):
    return sum(args)


mumeros = [2, 6, 5, 4, 8]
# desempacotando a lista
print(soma_todos(*mumeros))




