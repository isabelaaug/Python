"""
Por que testar nosso codigo...

-Reduzir bugs
-Reduz as chances de que recursos novos quebrem (alterem) recursos existentes
-Garantem que problemas que ja foram corrigidos, permanecem corrigidos

TDD - Test Driven Development (Desenvolvimento Guiado por Teste)

"""


class Gato:

    def __init__(self, nome):
        super().__init__(nome)

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        print(f'{self.__nome} fala miau!')


felix = Gato('Felix')
felix.falar()
print(felix.nome)
