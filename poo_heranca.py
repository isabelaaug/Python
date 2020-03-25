"""
Heranca (Inheritance)

- Reaproveitamento de codigo e extensao de classes.

- A classe herdada eh conhecida como Super classe, classe mae, pai, base ou generica. [Pessoa]
- A classe que recebe a heranca eh conhecida coo sub classe, classe filha ou especifica.[cliente, funcionario]




class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

---------------------------------
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # indica a heranca

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # forma incomum de acessar a super classe
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # forma comum de acessar a super classe
        self.__matricula = matricula

-----------------------------------

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # indica a heranca

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # forma incomum de acessar a super classe
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # forma comum de acessar a super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Matricula: {self.__matricula} - Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Lucas', 'Costa', '152.256.185-20', 5600)
cliente2 = Cliente('Alef', 'Souza', '155.776.255-60', 1800)
func1 = Funcionario('Jose', 'Silva', '154.264.147-52', 8578)
func2 = Funcionario('Paulo', 'Pereira', '196.258.323-87', 8594)
print(cliente1.nome_completo())
print(func1.nome_completo())

-----------------------------

Metodo super() - refere a uma super classe


"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__nome} faz som {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        super().faz_som('miiiaaaaauuuu')
        self.__raca = raca


gato1 = Gato('Felix', 'felino', 'siames')
gato1.faz_som('miau')


