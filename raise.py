"""
Levantando erros com Raise

raise (palavra reservada) -- lança exceções
Sintaxe: raise TipoDoErro('Mensagem de erro')
-raise finaliza a função

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} será impresso na cor {cor}')


colore('isa', 'azul')  # o texto isa será impresso na cor azul
colore('isa', 43)  # TypeError: cor precisa ser uma string

------------------------------------------------


"""


def colore(texto, cor):
    cores = ('verde', 'vermelho', 'cinza', 'preto')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'a cor precisa ser uma entre: {cores}')
    print(f'o texto {texto} será impresso na cor {cor}')


colore('isa', 'azul')  # ValueError: a cor precisa ser uma entre: ('verde', 'vermelho', 'cinza', 'preto')







