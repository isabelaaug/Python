"""
Lambdas

-são funções sem nome, ou seja, anônimas. Sintaxe: <nome> = lambda <parâmetros>: <função>

Ex:
# Função normal em Python
def funcao(x):
    return 3 * x + 1


print(funcao(2))  # 7

# Função lambda em Python
calc = lambda x: 3 * x + 1


print(calc(2))  # 7

----------------------------------
strip() -- retira espaços do inicio e fim da string

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('isabela augusta', ' de OLIVEIRA'))  # Isabela Augusta De Oliveira

-------------------------------

py = lambda: 'Como não amar Python?'
print(py())  # Como não amar Python?

------------------------------

obs: ele faz a ordenação pelo sobrenome, selecionando o ultimo elemento [-1]
autores = ['Isaac Asimov', 'Arthur C. Clarke', 'Orson Scott Card', 'H. G. Wells']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


"""

# Função quadradatica  --  ax^2 + bx + c


def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(2, 3, -5)
print(teste(2))
print(funcao_quadratica(2, 3, -5)(2))

