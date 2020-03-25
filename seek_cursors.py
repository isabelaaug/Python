"""
Seek e cursors

seek() - é utilizada para movimentar o cursor pelo arquivo
streaming - conexão entre o programa e o arquivo e o clone() é utilizado para finalizar isso

arquivo = open('texto.txt')
print(arquivo)
print(arquivo.read())
arquivo.seek(0)  # retorna o cursor para a primeira posição
print(arquivo.read())

----------------

arquivo = open('texto.txt')
print(arquivo.readline())  # realiza a leitura da primeira linha
print(arquivo.readline())  # realiza a leitura da segunda linha
print(arquivo.readline())  # realiza a leitura da terceira linha

----------------------
arquivo = open('texto.txt')
ret = arquivo.readline()
print(ret)  # realiza a leitura da primeira linha
print(ret.split(' '))  # cria uma lista separando a primeira linha por espaços

-------------------

arquivo = open('texto.txt')
ret = arquivo.readlines()  # cria uma lista separando cada linha em um item
print(len(ret))  # conta quantas linhas

----------------------------

arquivo = open('texto.txt')
print(arquivo.read())
arquivo.close()
print(arquivo.closed)  # verifica se o arquivo foi fechado

-------------------

arquivo = open('texto.txt')
print(arquivo.read(40))  # limita a leitura aos primeiros 40 caracteres
arquivo.close()
print(arquivo.closed)  # verifica se o arquivo foi fechado

"""






