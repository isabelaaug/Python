"""
Metodos

- metodo - comportamento do objeto (funcoes)

- nome em minusculo: casa_azul

2 grupos:

Metodo de instancia:

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        Retorna o valor do produto com desconto
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto('Xone', 'Video game', 1100)
p2 = Produto('PS4', 'Video game', 2500)

print(p1.desconto(50))
print(Produto.desconto(p1, 50))

user1 = Usuario('lucas', 'augusto', 'lu@gmail.com', '415654')
user2 = Usuario('laura', 'oliveira', 'lara@gmail.com', '3433')

print(user1.nome_completo())
print(user2.nome_completo())
print(f'Senha User1: {user1._Usuario__senha}')
print(f'Senha User2: {user2._Usuario__senha}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        Retorna o nome completo do usuario
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe o seu nome: ')
sobrenome = input('Informe o seu sobrenome: ')
email = input('Informe o seu emal: ')
senha = input('Informe o seu senha: ')
confirma_senha = input('Informe o seu senha novamente: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('senha nao confere.')

print('usuario criado com sucesso')

senha = input('Informe a senha: ')

if user.checar_senha(senha):
    print('acesso permitido')
else:
    print('acesso negado')

print(f'Senha User: {user._Usuario__senha}')

----------------------------

Metodos de classe  -- metodos estaticos em outras linguagens

Criamos um metodo de instancia quando precisamos acessar um atributo de instancia (self)
metodos de classe apenas acessam atributos de classe (cls)

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # metodo de classe
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('oi')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        Retorna o nome completo do usuario
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user1 = Usuario('lucas', 'augusto', 'lu@gmail.com', '415654')
user2 = Usuario('laura', 'oliveira', 'lara@gmail.com', '3433')
Usuario.conta_usuarios()

--------------------------------

Metodos privados  -- duplo underline no nome

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # metodo de classe
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('oi')


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        Retorna o nome completo do usuario
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user1 = Usuario('lucas', 'augusto', 'lu@gmail.com', '415654')
user2 = Usuario('laura', 'oliveira', 'lara@gmail.com', '3433')
Usuario.conta_usuarios()
print(user1._Usuario__gera_usuario())
print(user2._Usuario__gera_usuario())

----------------------------------------------

Metodos estaticos -- nao tem acesso a classe ou instancia

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # metodo de classe
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('oi')

    @staticmethod
    def definicao():
        return 'NADA'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        Retorna o nome completo do usuario
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user1 = Usuario('lucas', 'augusto', 'lu@gmail.com', '415654')
user2 = Usuario('laura', 'oliveira', 'lara@gmail.com', '3433')
Usuario.conta_usuarios()
print(user1._Usuario__gera_usuario())
print(user2._Usuario__gera_usuario())
print(Usuario.definicao())
print('--')
print(user1.definicao())

"""

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, tensao, cor, luminosidade):  # metodo construtor
        self.__tensao = tensao
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):  # metodo de classe
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('oi')

    @staticmethod
    def definicao():
        return 'NADA'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        """Retorna o nome completo do usuario"""
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user1 = Usuario('lucas', 'augusto', 'lu@gmail.com', '415654')
user2 = Usuario('laura', 'oliveira', 'lara@gmail.com', '3433')
Usuario.conta_usuarios()
print(user1._Usuario__gera_usuario())
print(user2._Usuario__gera_usuario())
print(Usuario.definicao())
print('--')
print(user1.definicao())
