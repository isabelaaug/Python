"""
Metodos Magicos (metodos que usam dunder - __metodo__ ) - todos vem da classe object


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # Representacao do objeto
        return f'{self.titulo} escrito por {self.autor}'

    OU

    def __str__(self):  # Representacao do objeto
        return f'{self.titulo} escrito por {self.autor}'


livro1 = Livro('Harry Potter', 'JK Rolling', 500)
livro2 = Livro('Brida', 'Paulo Coelho', 200)

print(livro1)  # Harry Potter
print(livro2)  # Brida

"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):  # Representacao do objeto
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):  # define o que sera medido
        return self.paginas

    def __del__(self):
        print('objeto foi deletado')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Nao eh possivel multiplicar'


livro1 = Livro('Harry Potter', 'JK Rolling', 500)
livro2 = Livro('Brida', 'Paulo Coelho', 200)

print(livro1)  # Harry Potter
print(livro2)  # Brida
print(len(livro1))  # 500
# del livro2
print(livro1.__dict__)
print(livro2.__dict__)
print(livro1 + livro2)
print(livro1 * 5)
