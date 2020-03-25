"""
Tipo numerico

5/2 = 2.5 -- resulta em um numero real
5//2 = 2 -- resulta em um numero inteiro (int(5/2))
5 % 2 = 1 -- modulo ou resto da divisão
2 ** 2 = 4 -- potência (2^2)
1_000_000 = 1000000 -- facilita visualização
num = 2
num + 1 = 3 -- serve apenas para um calculo
num += 1 = 3 ou num = num + 1 = 3 -- incrementa a variável
type(num)
<class 'int'>

dupla atribuição:

valor1, valor2 = 2, 3

----------------------------------

tipo float / real / decimal
valor = 2.3
numero complexo
23j -- numero+j

arredondar float:
num = 3.143424332
num_2 = round(num, 2)

print(num)
print(num_2)

-----------------------------

tipo Booleano

True or False
ativo = True

Negação (NOT)
print(not ativo) -- False

Ou (or)
T OR T = T
T OR F = T
F OR T = T
F OR F = F

E (And)
T E T = T
T E F = F
F E T = F
F E F = F

-------------------------

TIPO String

frase = 'isabela augusta"
print(frase.split()) = 'isabela''augusta'-- transforma em uma lista vetor[0-...] frase[0-6]
print(frase.split()[0]) = 'isabela'
print(frase.split()[1]) = 'augusta'
print(frase[0:3]) = isa -- slice de string

inverte a string
print(frase[::-1]) -- vai do primeiro ao ultimo elemento e inverte

substitui caracteres
print(frase.replace('i','y') = ysabela

----------------------

Escopo de variaveis
variaveis globais e locais

- se temos duas variaveis com o mesmo nome, a varialvel local irá sobrepor a global em uma função
- funçoes necessitam de variaveis locais, do contrario é necessário avisar  com 'global <nome_variavel_global>'
def diz_oi(instrutor):
    instrutor = 'isa'
    return f'oi {instrutor}'

instrutor = 'bela'
print(diz_oi(instrutor))


---------------------------------
Tipo NONE
tipo sem tipo (class 'NoneType') ou tipo vazio
é sempre especificado com a primeira maiuscula
podemos utiliza la quando não sabemos qual será seu valor final

numeros = None


"""
num_1 = int(input('Digite um inteiro: '))
print(f'O inteiro digitado foi {num_1}')

num_2 = float(input('Digite um numero real: '))
print(f'O numero digitado foi {num_2}')

num_31 = int(input('Digite o primeiro numero: '))
num_32 = int(input('Digite o segundo numero: '))
num_33 = int(input('Digite o terceiro numero: '))
print(f'A soma é igual a {num_31 + num_32 + num_33}')

num_4 = float(input('Digite um numero: '))
print(f'O quadrado desse numero é igual a {num_4 ** 2}')

num_5 = float(input('Digite um numero: '))
print(f'A quinta parte desse numero é igual a {num_5 / 5}')

num_6 = float(input('Digite uma temperatura em graus Celsius: '))
print(f'Conversão para Fahrenheit: {num_6 * (9 / 5) + 32}')


