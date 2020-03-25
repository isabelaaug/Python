"""
Modos de abertura de arquivo

https://docs.python.org/3/library/functions.html#open

r - leitura
w - escrita
x - abre para a escrita somente se o arquivo noo existir - FileExistsError
a - abre para escrita adicionando o conteudo SEMPRE no final do arquivo

-------------------

try:
    with open('texto.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo')
except FileExistsError:
    print('arquivo ja existe')

------------
with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

----------------


"""

with open('fruta.txt', 'w+') as arquivo:
    arquivo.seek(0)
    arquivo.write('teste.\n')




