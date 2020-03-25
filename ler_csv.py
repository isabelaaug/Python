"""
Lendo CSV - Comma Separeted Values - Valores Separados por Virgula

Separadores: , ; <espaco>

with open('original.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

--- Modos de leitura de arquivos CSV:
- reader - permite que iteremos sobre as linhas do arquivo CSV como listas
- DictReader - permite que iteremos sobre as linhas do arquivo como OrderedDicts

# Reader

from csv import reader

with open('original.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pula uma linha
    for linha in leitor_csv:
        # Cada linha eh uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}cm')

# DictReader

from csv import DictReader

with open('original.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha eh uma lista
        print(f'{linha["Nome"]} nasceu no(a) {linha["Pais"]} e mede {linha["Altura (em cm)"]}cm')

# Declarando o separador

from csv import reader

with open('original.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')
    next(leitor_csv)  # pula uma linha
    for linha in leitor_csv:
        # Cada linha eh uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}cm')



"""

