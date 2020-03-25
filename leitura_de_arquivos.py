"""
Leitura de Arquivos

https://docs.python.org/3/library/functions.html#open

open() - abre arquivos -recebe nome do arquivo  e retorna um _io.TextIOWrapper

"""
arquivo = open('texto.txt')
print(arquivo)
print(arquivo.read())
print(arquivo.read())
