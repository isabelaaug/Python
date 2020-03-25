"""
Sistema de arquivos = Manipulacoes

https://docs.python.org/3/library/os.html#open

# Descobrindo se um arquivo existe

import os

print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('fruta.txt'))  # True

# Descobrindo se um diretorio existe

import os

print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university/geek1.py'))  # True

# criando arquivos

open('arquivo-teste1.txt', 'w').close()

open('arquivo-teste2.txt', 'a').close()

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

os.mknod('arquivo-teste4.txt')

# criando diretorios

os.mkdir('templates')

# criando arvore diretorios (se ja existir, nao da erro, ignora)

os.makedirs('templates/geek/university', exist_ok=True)

# renomeia arquivos

os.rename('arquivo-teste1.txt', 'arquivo-teste01.txt')

# renomeia diretorios vazios

os.rename('templates/geek', 'templates/testerename2')

# deleta arquivos (nao vao para a lixeira)

os.remove('arquivo-teste3.txt')

# deleta diretorios vazios

os.rmdir('templates/testerename2')

# deletanto arquivos ou diretorio e mandando para lixeira

from send2trash import send2trash

send2trash('arquivo-teste2.txt')

# Criando diretorio temporario com arquivo temporario (so existe enquanto o programa roda)

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()


# Criando arquivo temporario (so existe enquanto o programa roda)

import os
import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')  # arquivos temporarios so aceitam a escrita de bits
    tmp.seek(0)
    print(tmp.read())

import os
import tempfile

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

"""

# Criando diretorio temporario com arquivo temporario (so existe enquanto o programa roda)

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

