"""
Funções com retorno

-A diferença entre usar um print e o return esta em que temos a opção de apenas imprimir o resultado da função
ou não.
-return finaliza a função

def quadrado_de_7():
    print(7 * 7)  # o print esta implicito, será executado assim que a função é chamada

def quadrado_de_7():
    return 7 * 7  # a função devolve o resultado e o print é opcional

quadrado_de_7()
ret = quadrado_de_7()
print(f'retorno: {quadrado_de_7()}')
print(f'retorno: {ret}')

def diz_oi():
    print('teste')
    return 'oi'


print(diz_oi())

------------------------------------

def nova_funcao():
    variavel = False  # True / None / False
    if variavel:
        return 4
    elif variavel is None:
        return 2.5
    return 'b'


ret = nova_funcao()
print(ret)

-------------------------------
def nova_funcao():
    return 'b', 2, 4, 6


num1, num2, num3, num4 = nova_funcao()
print(num1, num2, num3, num4)
------------------------------

from random import random
# from funcoes_com_retorno import joga_moeda


def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

-------------------------------------
Funções com parâmetro

def quadrado(num):
    return num ** 2


print(quadrado(5))
ret = quadrado(8)
print(ret)


def parabens(nome):
    print(f'Parabens {nome}')


parabens('Isabela')

--------------------

def nome_completo(nome, sobrenome):
    return f'Parabens {nome} {sobrenome}'


nome = 'isa'
sobrenome = 'aug'

print(nome_completo(sobrenome, nome))  # a ordem dos argumentos importa
print(nome_completo(nome='isa', sobrenome='aug'))  # utilizando KEYWORD ARGUENTS a ordem passa a não importar
print(nome_completo(sobrenome=sobrenome, nome=nome))

---------------------
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 8, 4, 7]
print(soma_impares(lista))
-----------------------------

Funçoes com parametro padrão -- default parameters
-onde a passagem de parametros é opcional

Ex 1:
print('isa')
print()

----------------------------
def exponencial(numero, expoente=2):  # passar um valor padrão para um parametro torna opcional sua atribuição
    return numero ** expoente


print(exponencial(2, 3))  # 2^3
print(exponencial(2))  # 2^2

-------------------------------
def mostra_info(nome='isa', instrutor=False):
    if nome == 'isa' and instrutor:
        return 'Bem vinda isa'
    elif nome == 'isa':
        return 'pensei que era a instrutora'
    return f'Olá {nome}'


print(mostra_info())  # pensei que era a instrutora
print(mostra_info(instrutor=True))  # Bem vinda isa
print(mostra_info(True))  # Olá True
print(mostra_info('isabela'))  # Olá isabela
print(mostra_info(nome='bela'))  # Olá bela

---------------------

def soma(a, b):
    return a + b


def subt(a, b):
    return a - b


def mat(a, b, fun=soma):
    return fun(a, b)


print(mat(34, 54))
print(mat(37, 43, subt))

---------------------------
total = 1


def incrementa():
    global total  # avisa que utilizara uma vaiavel global
    total = total + 1
    return total


print(incrementa())  # 2
print(incrementa())  # 3
print(incrementa())  # 4
-------------------------------
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())  # 1
print(fora())  # 1
print(fora())  # 1
-------------------------------


"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 8, 4, 7]
    print(soma_impares(lista))






