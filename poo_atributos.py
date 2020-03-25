"""
Atributos

atributo - caracteristica do objeto

3 grupos:

Atributos de instancia - sao declarados dentro do metodo construtor

- Por padrao todos os atributos publicos
- Atributos privados (so eh acessado dentro da propria classe) sao representados por __ no inicio do nome

class Lampada:

    def __init__(self, tensao, cor):  # metodo construtor
        self.tensao = tensao
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# atributos privados (so eh acessado dentro da propria classe)
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)

    def mostra_senha(self):
        print(self.__senha)


user = Acesso('user@gmail.com', '23232')
print(user.email)
print(user._Acesso__senha)  # acessando atributo privado
user.mostra_email()
user.mostra_senha()

----------------------------------

# Atributos de Classe - sao declarados diretamente na classe, fora do construtor

class Produto:

    imposto = 1.05  # atributo de classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Xone', 'Video game', 1100)
p2 = Produto('PS4', 'Video game', 2500)

print(p1.valor)
print(p2.valor)
print(Produto.imposto)  # 1.05
print(p1.id)
print(p2.id)

--------------------------------------

- Atributo dinamico - eh um atributo de instancia que pode ser criado em tempo de execucao





"""


class Lampada:

    def __init__(self, tensao, cor):  # metodo construtor
        self.tensao = tensao
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# atributos privados (so eh acessado dentro da propria classe)
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.email)

    def mostra_senha(self):
        print(self.__senha)


class Produto:

    imposto = 1.05  # atributo de classe
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Xone', 'Video game', 1100)
p2 = Produto('PS4', 'Video game', 2500)

p2.peso = '1kg'

print(f'produto: {p2.nome}, peso: {p2.peso}')  # produto: PS4, peso: 1kg
# print(f'produto: {p1.nome}, peso: {p1.peso}')  # AttributeError: 'Produto' object has no attribute 'peso'

# Deletando atributos

print(p1.__dict__)  # {'id': 1, 'nome': 'Xone', 'descricao': 'Video game', 'valor': 1155.0}
print(p2.__dict__)  # {'id': 2, 'nome': 'PS4', 'descricao': 'Video game', 'valor': 2625.0, 'peso': '1kg'}

del p2.nome
del p2.peso
print(p2.__dict__)  # {'id': 2, 'descricao': 'Video game', 'valor': 2625.0}






