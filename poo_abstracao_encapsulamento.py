"""
Abstracao e Encapsulamento

Abstracao eh o ato de expor apenas os dados relevantes de uma classe, escondendo atributos e metodos privados.



"""


class Conta:
    contador = 4999

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
