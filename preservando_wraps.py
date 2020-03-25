"""

Preservando metadatas com wraps

metadatas - sao dados intrisecos em arquivos (descricao, por exemplo)
wraps - sao funcoes que envolvem elementos diversos

def ver_log(funcao):
    def logar(*args, **kwargs):
        Eu sou uma funcao dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    Soma dois numeros
    return a + b


print(soma(10, 23))  # Voce esta chamando soma / Aqui a documentacao: Soma dois numeros / 33

print(soma.__name__)  # logar
print(soma.__doc__)  # Eu sou uma funcao dentro de outra

------------------------------------


"""

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(10, 23))  # Voce esta chamando soma / Aqui a documentacao: Soma dois numeros / 33
print('--')
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros
