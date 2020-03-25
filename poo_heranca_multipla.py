"""
Heranca Multipla

- heranca de varias classes com todos os metodos e atributos
- quando nao especificado a classe herda object


--- Multiderivacao direta

class Base1:
    pass


class Base2:
    pass


class Multiderivada(Base1, Base2):
    pass

--- Multiderivacao indireta

class Base01:
    pass


class Base02(Base01):
    pass


class Base03(Base02):
    pass


class Multiderivada(Base03):
    pass


"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Oi!! Eu sou {self.__nome}.'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando...'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} um animal do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando...'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} um animal terrestre!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Willie')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Robert')
print(tatu.andar())
print(tatu.cumprimentar())

ping = Pinguim('Julio')
print(ping.andar())
print(ping.nadar())
print(ping.cumprimentar())  # Method Resolution Order - MRO

print(f'Ping eh instancia de Pinguins? {isinstance(ping, Pinguim)}')  # True
print(f'Ping eh instancia de Aquatico? {isinstance(ping, Aquatico)}')  # True
print(f'Ping eh instancia de Terrestre? {isinstance(ping, Terrestre)}')  # True
print(f'Ping eh instancia de Animal? {isinstance(ping, Animal)}')  # True
print(f'Ping eh instancia de Object? {isinstance(ping, object)}')  # True
