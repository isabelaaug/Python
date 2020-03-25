"""
StringIO

- utilizado para ler e criar arquivos em memoria


"""
from io import StringIO

mensagem = 'String Normal'

# Podemos criar um arquivo em memoria ja com uma string inserida ou vazia

arquivo = StringIO(mensagem)  # == arquivo = open('arquivo.txt', 'w')
print(arquivo.read())
arquivo.write(' mais textos')
arquivo.seek(0)
print(arquivo.read())





