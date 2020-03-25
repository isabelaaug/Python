"""
Sorted

- função para ordenar
- não altera a lista original, pois cria uma nova
- sempre retorna uma lista, mesmo que esteja organizandou uma tupla ou set

numeros = [6, 8, 9, 15, 2, 3, 1]
print(numeros)  # [6, 8, 9, 15, 2, 3, 1]
print(sorted(numeros))  # [1, 2, 3, 6, 8, 9, 15]
print(numeros)  # [6, 8, 9, 15, 2, 3, 1]

nova = sorted(numeros)
print(nova)  # [1, 2, 3, 6, 8, 9, 15]

-------------------------

# adicionado parâmetros
numeros = [6, 8, 9, 15, 2, 3, 1]
print(sorted(numeros, reverse=True))  # [15, 9, 8, 6, 3, 2, 1] - ordena do maior para o menor
print(set(sorted(numeros)))  # {1, 2, 3, 6, 8, 9, 15}
print(tuple(sorted(numeros)))  # (1, 2, 3, 6, 8, 9, 15)

----------------------------


usuarios = [
    {'username': 'samuel', 'tweets': ['Eu acordei', 'Bate bola, jogo rapido']},
    {'username': 'lucas', 'tweets': ['Bate palma']},
    {'username': 'joao', 'tweets': []},
    {'username': 'lari', 'tweets': []},
    {'username': 'amanda', 'tweets': ['Eu sei, vc nao', 'fala mais q ta pouco', 'abre o jogo rapido']}
    ]

print(sorted(usuarios, key=len))  # conta a quantidade de elementos e ordena do menor para o maior
print(sorted(usuarios, key=lambda usuario: usuario['username']))  # organiza em ordem alfabetica os usuarios
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))  # quant. de tweets e ordena do menor para o maior


"""

musicas = [
    {'titulo': 'quarta cadeira', 'tocou': 8},
    {'titulo': 'beija flor', 'tocou': 2},
    {'titulo': 'paradinha', 'tocou': 15},
    {'titulo': 'menina solta', 'tocou': 5}
]

# ordena da menos para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))


