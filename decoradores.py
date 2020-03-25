"""
Decoradores - Decorators

-

def seja_educado(funcao):
    def sendo():
        print('Fala ai')
        funcao()
        print('vai na paz')
    return sendo


def saudacao():
    print('Seja bem vindo')


teste = seja_educado(saudacao)
teste()

----------------------------------------
# Syntax Sugar

def seja_educado(funcao):
    def sendo():
        print('Fala ai')
        funcao()
        print('vai na paz')
    return sendo


@seja_educado
def apresentacao():
    print('Sou isa')


apresentacao()

----------------------------------------
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def quem(nome):
    return f'Sou {nome}'


@gritar
def solicitar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


print(quem('isa'))
print(solicitar('bife', 'batata'))
print(solicitar(acompanhamento='pizza', principal='refri'))

--------------------------------

def verifica_primeiro_arg(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento tem que ser {valor}'
            return funcao (*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_arg('agua')
def comida_favorita(*args):
    return args


@verifica_primeiro_arg(10)
def soma_dez(n1, n2):
    return n1 + n2


print(comida_favorita('agua', 'bolo'))
print(comida_favorita('pizza', 'feijao'))
print(soma_dez(15, 50))
print(soma_dez(10, 18))

------------------------------------

Forcando tipos de dados com decoradores



"""


def forcar_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forcar_tipo(str, int)
def repete(msg, vezes):
    for vez in range(vezes):
        print(msg)


print(repete(55, 2.5))


@forcar_tipo(float, float)
def dividir(a, b):
    print(a/b)


print(dividir('8', 6))



