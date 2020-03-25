"""
Polimorfismo - varias formas

Overiding - sobescrita de metodo
Polimorfismo eh sobre escrever um metodo


"""
from abc import ABC


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    # obriga a implementacao do metodo
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo!')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala nada, eh um rato!')


bob = Cachorro('Bob')
bob.comer()
bob.falar()
felix = Gato('Felix')
felix.comer()
felix.falar()
kiko = Rato('Kiko')
kiko.comer()
kiko.falar()
