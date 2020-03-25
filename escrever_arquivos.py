"""
Escrevendo em arquivos

with open('novo.txt', 'w') as arquivo:  # w - white e cria o arquivo ou abre o xistente com esse nome
    arquivo.write('Joga com delicadeza.\n' * 12)  # subscreve os dados do arquivo
    arquivo.write('Ela bate o bumbum no bumbo.')

with open('texto.txt') as arquivo:  # w - white
    arquivo.seek(0)
    print(arquivo.read())



"""

with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('informe uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break




