"""
Pickle e Json (JavaScript Object Notation)
API - meios de comunicacao entre servicos de empresas e terceiros

ret = json.dumps(['Produto', {'Xone': ('1TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)  # ["Produto", {"Xone": ["1TB", "Novo", "220V", 2340]}]

--------------------------

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'siames')
print(felix.__dict__)  # {'_Gato__nome': 'Felix', '_Gato__raca': 'siames'}
ret = json.dumps(felix.__dict__)
print(ret)  # {"_Gato__nome": "Felix", "_Gato__raca": "siames"}

--------------------------

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'siames')
ret = jsonpickle.encode(felix)
print(ret)  # {"_Gato__nome": "Felix", "_Gato__raca": "siames", "py/object": "__main__.Gato"}

--------------------------------------

# Escrevendo o arquivo JSON
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'siames')
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

-------------------------



"""

import jsonpickle


# lendo o arquivo JSON
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)
    print(type(ret))
