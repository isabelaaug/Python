"""
Counter - contador
Collections - High performance container datatypes
https://docs.python.org/3/library/collections.html
# coloca os elementos como chave e o valor é a quantidade de repetiçao de cada elemento
lista = [1, 2, 2, 2, 4, 5, 3, 3, 3, 3, 1, 2, 5]
res = Counter(lista)  # Counter({2: 4, 3: 4, 1: 2, 5: 2, 4: 1})
print(res)

print(Counter('isa aug'))  # Counter({'a': 2, 'i': 1, 's': 1, ' ': 1, 'u': 1, 'g': 1})

"""
from collections import Counter

# conta quantas vezes uma palavra se repete
texto = """Texto é um conjunto de palavras e frases encadeadas que permitem interpretação e transmitem 
uma mensagem. É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito. 
Um texto é uma unidade linguística de extensão superior à frase."""
palavras = texto.split()

res = Counter(palavras)
print(res)

# indica as 3 palavras mais comuns
print(res.most_common(3))


