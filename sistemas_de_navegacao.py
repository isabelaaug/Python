"""
Sistema de navegacao

os - sistema operacional

import os

#  retorna o diretorio atual do programa
print(os.getcwd())  # C:\Users\\isabe\\PycharmProjects\\guppy
# para mudar o diretorio, voltando um nivel da raiz
os.chdir('..')
print(os.getcwd())  # C:\Users\\isabe\\PycharmProjects
print(os.path.isabs('C:\\Users\\isabe\\PycharmProjects'))  # True ou false,
checa se o diretorio é absoluto ou relativo


print(os.name)  # posix (linux e mac) ou nt (windows)
print(os.uname)  # posix (linux e mac) ou nt (windows) informacao mais completa



"""
import os
print(os.getcwd())



