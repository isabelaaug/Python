"""
Method Resolution Order - MRO

- a sequencia que as classes sao declaradas como heranca fazem diferenca
- eh necessario declara da principal para a menos importante



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


ping = Pinguim('Julio')
print(ping.cumprimentar())  # Method Resolution Order - MRO
