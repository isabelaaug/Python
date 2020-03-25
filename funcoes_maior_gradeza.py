"""
Funcoes de maior grandeza - first class citizan

- sao funcoes que podem retornar outras funcoes

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(3, 5, soma))

------------------------

Nested function - funcoes alinhadas

from random import choice


def ola(pessoa):
    def humor():
        return choice(('oi, ', 'fala ai, ', 'opa, '))
    return humor() + pessoa


print(ola('isa'))
print(ola('marco'))


Retornando funcoes de outras funcoes
from random import choice


def dinheiro():
    def rir():
        return choice(('kkkk', 'hahaha', 'shshsshs'))
    return rir()


rindo = dinheiro()
print(rindo)



"""
from random import choice


def faz_risada(pessoa):
    def dando_risada():
        risada = choice(('kkkk', 'hahaha', 'shshsshs'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_risada(' isa')
print(rindo())


