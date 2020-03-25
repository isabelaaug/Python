"""
Pacotes

- É um diretorio com uma coleção de módulos

"""

from geek import geek1
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(3, 5))

from geek.geek1 import funcao1
print(funcao1(3, 4))
