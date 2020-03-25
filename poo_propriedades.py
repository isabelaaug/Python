"""
Propriedades - Properties

Getters - retornam o valor do atributo
Setters - alteram o valor do atributo

class Conta:

    contador = 5000

    def __init__(self, titular, limite, saldo):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        Conta.contador = self.__numero

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('o valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if valor < self.__saldo:
                self.__saldo -= valor
            else:
                print('saldo insuficiente')
        else:
            print('o valor deve ser positivo')

    def transferencia(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_numero(self, numero):
        self.__numero = numero

    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('isa', 1000, 8800)
conta2 = Conta('joao', 5260, 10000)

print(conta1.__dict__)
print(conta2.__dict__)
conta1.transferencia(100, conta2)
print(conta1.__dict__)
print(conta2.__dict__)
conta1.sacar(500)
conta2.depositar(500)
print(conta1.__dict__)
print(conta2.__dict__)

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas eh {soma}')
print(conta2.__dict__)
conta2.set_limite(1000)
print(conta2.__dict__)

------------------------


"""


class Conta:

    contador = 5000

    def __init__(self, titular, limite, saldo):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        Conta.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('o valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if valor < self.__saldo:
                self.__saldo -= valor
            else:
                print('saldo insuficiente')
        else:
            print('o valor deve ser positivo')

    def transferencia(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('isa', 1000, 8800)
conta2 = Conta('joao', 5260, 10000)

""" print(conta1.__dict__)
print(conta2.__dict__)
conta1.transferencia(100, conta2)
print(conta1.__dict__)
print(conta2.__dict__)
conta1.sacar(500)
conta2.depositar(500)
"""

print(conta1.__dict__)
print(conta2.__dict__)
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas eh {soma}')
print(conta1.__dict__)
conta1.limite = 8000
print(conta1.__dict__)
print(conta1.limite)
print(conta1.valor_total)

