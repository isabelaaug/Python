"""
Conhecendo **kwargs
-exige a utilização de parâmetros nomeados e tranforma os parametros extras em dicionários
-**kwargs e *args não são parâmetros obrigatórios

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marco='verde', julia='amarelo', fernanda='azul')


def cumprimento(**kwargs):
    if 'isa' in kwargs and kwargs['isa'] == 'python':
        return 'voce recebeu um ola'
    elif 'isa' in kwargs:
        return f'{kwargs["isa"]} Geek'
    return 'não sei'


print(cumprimento())  # não sei
print(cumprimento(isa='python'))  # voce recebeu um ola
print(cumprimento(isa='oi'))  # oi Geek
print(cumprimento(isa='especial'))  # especial Geek

-----------------
Em funções os parâmetros são declarados na seguinte sequencia:

- obrigatórios
- *args
- default
- **kwargs

Ex:
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(19, 'Pedro', 4, 5, 3, solteiro=True)
minha_funcao(23, 'Taina', eu='Nao', voce='Vai')
minha_funcao(12, 'Laura', 9, 4, 3, java=False, python=True)

---------------------------

# Desempacotando dicionários


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felipe', 'sobrenome': 'Joao'}

print(mostra_nomes(**nomes))

---------------------------------


"""


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)  # nomes devem ser os mesmos dos parametros para funcionar o desempacotamento
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)


