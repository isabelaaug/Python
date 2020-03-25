"""
Dunder name e main

dunder - double underline

dunder name -> __name__
dunder main -> __main__

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 8, 4, 7]
    print(soma_impares(lista))

from funcoes_com_retorno import soma_impares
print(soma_impares([5, 6, 1]))

"""
import primeiro  # primeiro importado

