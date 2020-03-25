"""
Bloco With

- é utilizado para criar um contexto de trabalho onde os recursos são fechado após

"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())



