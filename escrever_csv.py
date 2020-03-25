"""
Escrevendo em Arquivos CSV

reader() leitor, writer() escritorem minutos

writerow() - escreve uma linha

with open('filmes.csv', 'w', newline='') as arquivo:  # ou 'a' se o arquivo ja existir
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao em minutos'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duracao em minutos do filme: ')
            escritor_csv.writerow([filme, genero, duracao])

-------------------------------



"""

from csv import DictWriter

# o cabecalho e as chaves precisam ser exatamente iguais

with open('filmesdict.csv', 'w', newline='') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao em minutos']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duracao em minutos do filme: ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao em minutos': duracao})
