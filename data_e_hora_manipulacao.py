"""
Manipulando Data e Hora

import datetime


print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now())  # 2020-03-11 20:30:21.523805
print(repr(datetime.datetime.now())) # ano, mes, dia, hora, minuto, segundo, microsegundo
inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(hour=16, minute=15, second=0, microsecond=12)
print(inicio)  # 2020-03-11 16:15:00.000012

# convertendo data

evento = datetime.datetime(2021, 1, 1, 0)
print(evento)  # 2021-01-01 00:00:00
nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

"""

import datetime


# Acessando os elementos
evento = datetime.datetime.now()
print(evento.year)  # 2020
print(evento.month)  # 3
print(evento.day)  # 11



