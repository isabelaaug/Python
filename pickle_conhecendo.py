"""
Conhecendo o Pickle

- Tem funcao de serializar e desserializar um objeto Python por meio da binarizacao
- nao eh seguro quanto a dados maliciosos

-- Escrita de arquivo .pickle

felix = Gato('Felix')
bob = Cachorro('Bob')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, bob), arquivo)

-- Leitura de arquivo .pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama se {gato.nome}')
    gato.mia()
    print(f'O gato eh {type(gato)}')
    print(f'O cachorro chama se {cachorro.nome}')
    cachorro.late()
    print(f'O gato eh {type(cachorro)}')

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} esta comendo...')

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo...')


with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama se {gato.nome}')
    gato.mia()
    print(f'O gato eh {type(gato)}')
    print(f'O cachorro chama se {cachorro.nome}')
    cachorro.late()
    print(f'O gato eh {type(cachorro)}')
