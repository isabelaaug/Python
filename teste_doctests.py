"""
Doctests

- sao testes que colocamos na docstring das funcoes/metodos
- nao reconhece string com aspas duplas
- qualquer "espaco" ou caracter no resoltado esperado pode gerar falha no teste

No terminal: -m doctest -v nome_do_modulo.py

def soma(a, b):
    ###soma os valores
    #>>> soma(1, 2)
    3
    ###

    return a + b


print(soma(3, 4))  # 7

--------------------------------------

Red

def duplicar(valores):
    ###duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    ###
    pass

----------
Refector

def duplicar(valores):
    ###duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    ###
    return [2 * elemento for elemento in valores]

----------------------------------------

def fala_oi():
    ###Fala Oi

    #>>> fala_oi()
    'oi'
    ###
    return 'oi'



"""


def fala_verdade():
    """Fala verdade

    >>> fala_verdade()
    True
    """
    return True

