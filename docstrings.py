"""
Documentando funções com docstrings
- documentação das funções

No terminal:
from docstrings import diz_oi
print(diz_oi.__doc__)
help(diz_oi)


"""


def diz_oi():
    """uma funcao que retorna oi"""
    return 'Oi!'


def exponencial(num, expoente=2):
    """
    Funçao que por padrao eleva o numero ao quadrado
    :param num: valor
    :param expoente: expoente que elevara o valor
    :return: resultado
    """
    return num ** expoente

