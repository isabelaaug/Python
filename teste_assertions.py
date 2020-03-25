"""
Assertions (Checagens/ Questionamentos)

- checa se uma expressao eh valida (None) ou nao (AssertionError)

def soma_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos precisam ser positivos'
    return a + b


ret = soma_positivos(-4, 5)
print(ret)  # AssertionError: Ambos precisam ser positivos

Executando no terminal: pytohn -O <nome do programa>.py cancela a checagem do assert (flag -O)

"""


def soma_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos precisam ser positivos'
    return a + b


ret = soma_positivos(4, 5)
print(ret)


def comer_fastfood(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'batata frita'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fastfood(comida))

