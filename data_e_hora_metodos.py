"""
Metodos de Data e Hora

import datetime

agora = datetime.datetime.now()  # permite especificar um fuso horario (time zone)
hoje = datetime.datetime.today()
print(hoje)

---------------------------

# mudancas ocorrendo a meia noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(repr(manutencao))

---------------------------

# encontrar o dia da semana que o evento ocorreu
# 0 - segunda, 1 - terca, 2 - quarta, 3 - quinta, 4 - sexta, 5 - sabado e 6 - domingo
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())  # 3
print(repr(manutencao))

--------------------------------------

# encontrar o dia da semana que nasceu

nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
if nascimento.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif nascimento.weekday() == 1:
    print('Voce nasceu em uma terca-feira')
elif nascimento.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif nascimento.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif nascimento.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif nascimento.weekday() == 5:
    print('Voce nasceu em um sabado')
elif nascimento.weekday() == 6:
    print('Voce nasceu em um domingo')

----------------------------

# Formatando data e hora

hoje = datetime.datetime.today()
print(hoje)  # 2020-03-11 23:26:45.540825
hoje_formatado = hoje.strftime('%d/%m/%y')  # Y - 2020 ou y - 20 / m - 03 ou b - Mar ou B - March
print(hoje_formatado)  # 11/03/20

------

import datetime


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Marco de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.mouth == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.mounth == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


# Formatando data e hora
hoje = datetime.datetime.today()
print(formata_data(hoje))  # 11 de Marco de 2020

-------
https://textblob.readthedocs.io/en/dev/
import datetime
from textblob import TextBlob


def formata_data(data):
    return f" {data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


# Formatando data e hora
hoje = datetime.datetime.today()
print(formata_data(hoje))  # 11 de marcha de 2020

-------

nascimento = datetime.datetime.strptime('10/04/1995', '%d/%m/%Y')
print(nascimento)
niver = input('Informe sua data de nascimento (dd/mm/aaaa): ')
niver = datetime.datetime.strptime(niver, '%d/%m/%Y')
print(niver)

--------------------------------------

# Trabalhar somente hora
almoco = datetime.time(12, 30, 0)
print(almoco)

--------------

import timeit

# Marcando tempo de execucao do codigo
# Loop for
tempo1 = timeit.timeit('"-".join(str(n) for n in range (100))', number=1000)
print(tempo1)
# List
tempo2 = timeit.timeit('"-".join([str(n) for n in range (100)])', number=1000)
print(tempo2)
# Map
tempo3 = timeit.timeit('"-".join(map(str, range (100)))', number=1000)
print(tempo3)


"""

import timeit
import functools


# Marcando tempo de execucao do codigo
def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
