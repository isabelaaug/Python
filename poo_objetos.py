"""
Objetos

objeto - instancia da classe


"""

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, tensao, cor, luminosidade):  # metodo construtor
        self.__tensao = tensao
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

    def chaca_lamp(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz_oi(self):
        print(f'o cliente {self.__nome} diz oi')


class ContaCorrente:
    contador = 255847

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente eh {self.__cliente._Cliente__nome}')


cliente1 = Cliente('Isabela Oliver', '152456.258-36')
cc1 = ContaCorrente(5000, 10000, cliente1)
print(cc1.__dict__)
cc1.mostra_cliente()
cc1._ContaCorrente__cliente.diz_oi()


tensao = 220
cor = 'amarela'
luminosidade = 70

lamp1 = Lampada(220, 'branco', 60)
lamp2 = Lampada(tensao, cor, luminosidade)

print(f'A lampada esta ligada? {lamp1.chaca_lamp()}')
lamp1.ligar_desligar()
print(f'A lampada esta ligada? {lamp1.chaca_lamp()}')


