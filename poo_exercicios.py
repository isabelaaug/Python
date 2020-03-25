# Execicio 4


class Televisao:

    def __init__(self, ligada):  # metodo construtor
        self.ligada = ligada


class Controle:

    def __init__(self, canais, volume):
        self.__canais = canais
        self.__volume = volume

    def mudar_canal(self, valor):
        if valor > 0:
            self.__canais = valor
        else:
            print('canal invalido')

    def mudar_volume(self, valor):
        if valor < 0:
            self.__volume += valor
            print('aumentando volume')
        else:
            self.__volume -= valor
            print('diminuindo volume')


tv = 0

while True:
    if tv == 0:
        tv = input('Deseja ligar a tv? (sim) (nao): ')
        if tv == 'sim':
            tv1 = Televisao(tv)
            canal = int(input('Informe o canal: '))
            volume = int(input('Informe o volume: '))
            programacao1 = Controle(canal, volume)
            print(f'Configuracao atual da tv: {programacao1.__dict__}')
        else:
            print('Televisao desligada')
            break
    else:
        conf = int(input('Para mudar de canal [1] ou para mudar o volume [2] ou desligar [0]: '))

        if conf == 0:
            print('Televisao desligada')
            break

        if conf == 1:
            canal = int(input('Informe o canal: '))
            programacao1.mudar_canal(canal)
            print(f'Configuracao atual da tv: {programacao1.__dict__}')
        if conf == 2:
            volume = int(input('Informe o volume: '))
            programacao1.mudar_volume(volume)
            print(f'Configuracao atual da tv: {programacao1.__dict__}')




