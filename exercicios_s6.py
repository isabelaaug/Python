"""
EXERCICIOS SEÇÃO 6

1.
qntd = 5
valor = int(input(f'Informe o valor inicial: '))
x = 0

for n in range(1, qntd+1):
    if x == 0:
        mult = valor
        x = mult * 3
        print(f'Imprimindo {n}/{qntd}: {x}')
        res = x
    else:
        valor = res + x
        print(f'Imprimindo {n}/{qntd}: {valor}')
        res = res + x

qtd = 0
referencia = 1
while True:
    if referencia % 3 == 0:
        print(f'O {referencia} é múltiplo de 3')
        qtd += 1
    referencia += 1
    if qtd == 5:
        break

2.
for _ in range(3):
    for num in range(1, 101, 1):
        print(num, end='')
    print(' ')

3.
for num in range(10, 0, -1):
    print(num)
print('Fim')

4.
for num in range(0, 100001, 1000):
    print(num)
print('Fim')

5.
lista = []
count = 1
for _ in range(10):
    num = int(input(f'digite um numero ({count}/10): '))
    lista.append(num)
    count = count + 1
print(f'Soma: {sum(lista)}')

6.
lista = []
count = 1
for _ in range(10):
    num = int(input(f'digite um numero ({count}/10): '))
    lista.append(num)
    count = count + 1
print(f'Média Aritmética: {(sum(lista)) / 10}')

7.
lista = []
count = 1
valid = 0

for _ in range(5):
    num = int(input(f'digite um numero ({count}/5): '))
    count = count + 1
    if num > 0:
        lista.append(num)
        valid = valid + 1
print(count)
print(valid)
print(f'Média Aritmética: {(sum(lista)) / valid}')

8.
lista = []
cont = 0
qtd = int(input('quantos numeros voce deseja digitar ? : '))

for _ in range(qtd):
    num = int(input('digite um numero : '))
    lista.append(num)

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

9.
num = int(input(f'digite a quantidade de numeros impares desejada: '))
qtd = 0
referencia = 1

while True:
    if referencia % 2 > 0:
        print(f'O {referencia} é impar')
        qtd += 1
    referencia = referencia + 1
    if qtd == num:
        break

10.
lista = []
num = 50
qtd = 0
referencia = 1

while True:
    if referencia % 2 == 0:
        print(f'O {referencia} é par')
        lista.append(referencia)
        qtd += 1
    referencia = referencia + 1
    if qtd == num:
        break
print(sum(lista))

11.
num = int(input(f'digite um numero: '))
for count in range(0, num + 1):
    print(count)
print('Fim')

12.
num = int(input(f'digite um numero: '))
for count in range(num, -1, -1):
    print(count)
print('Fim')

13.
while True:
    referencia = int(input(f'digite um numero par: '))
    if referencia % 2 == 0:
        for count in range(1, referencia + 1):
            if count % 2 == 0:
                print(count)
        print(f'O {referencia} é par')
    else:
        print(f'{referencia} não é par')

14.
while True:
    referencia = int(input(f'digite um numero par: '))
    if referencia % 2 == 0:
        for count in range(referencia, 0, -1):
            if count % 2 == 0:
                print(count)
        print(f'O {referencia} é par')
    else:
        print(f'{referencia} não é par')

15.
while True:
    referencia = int(input(f'digite um numero impar: '))
    if referencia % 2 > 0:
        for count in range(1, referencia + 1):
            if count % 2 != 0:
                print(count)
        print(f'O {referencia} é impar')
    else:
        print(f'{referencia} não é impar')

16.
while True:
    referencia = int(input(f'digite um numero impar: '))
    if referencia % 2 > 0:
        for count in range(referencia, 0, -1):
            if count % 2 != 0:
                print(count)
        print(f'O {referencia} é impar')
    else:
        print(f'{referencia} não é impar')

17.
lista = []

num = int(input(f'digite um numero: '))
for count in range(1, num + 1):
    print(count)
    lista.append(count)

print(lista)
print(f'soma: {sum(lista)}')

18.
lista = []
qtd = int(input('quantos numeros voce deseja digitar ? '))

for count in range(qtd):
    num = int(input(f'digite o numero {count + 1}: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)
rep = lista.count(maior)
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

19.
n = int(input('Digite um número entre 100 e 999: '))
if 100 <= n <= 999:
    for _, c in enumerate(str(n)):
        print(c)
else:
    print('Número inválido!')

20.
listapar = []
listaimpar = []
par = 0
impar = 0
while True:
    referencia = int(input(f'digite um numero: '))
    if referencia != 1000:
        if referencia % 2 > 0:
            listaimpar.append(referencia)
            impar += 1
            print(f'O {referencia} é impar')
        if referencia % 2 == 0:
            listapar.append(referencia)
            par += 1
            print(f'O {referencia} é par')
    else:
        break
imparcount = len(listaimpar)
parcount = len(listapar)

print(f'numeros impares: {listaimpar}')
print(f'numeros pares: {listapar}')
print(f'quantidade de impares: {imparcount}')
print(f'quantidade de pares: {parcount}')

21.
lista1soma = []
lista2soma = []
lista1mult = []
lista2mult = []
par1 = 0
impar1 = 1
par2 = 0
impar2 = 1

ref1 = int(input(f'digite um numero: '))
ref2 = int(input(f'digite outro numero: '))

for count1 in range(1, ref1 + 1):
    if count1 % 2 == 0:
        lista1soma.append(count1)
        par1 = par1 + count1
    if count1 % 2 != 0:
        lista1mult.append(count1)
        impar1 = impar1 * count1
for count2 in range(1, ref2 + 1):
    if count2 % 2 == 0:
        lista2soma.append(count2)
        par2 = par2 + count2
    if count2 % 2 != 0:
        lista2mult.append(count2)
        impar2 = impar2 * count2

print(f'numeros pares: {lista1soma}')
print(f'numeros soma dos pares: {sum(lista1soma)}')
print(f'nnumeros soma dos pares: {par1}')
print(f'numeros impares: {lista1mult}')
print(f'numeros multiplicacao dos numeros impares: {impar1}')
print(f'numeros pares: {lista2soma}')
print(f'numeros soma dos pares: {sum(lista2soma)}')
print(f'numeros soma dos pares: {par2}')
print(f'numeros impares: {lista2mult}')
print(f'numeros multiplicacao dos numeros impares: {impar2}')

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
somapar = 0
multimpar = 1

for valor in range(a, (b + 1)):
    if valor % 2 == 0:
        somapar = somapar + valor
    else:
        multimpar = multimpar * valor
print(f'Soma dos pares é {somapar}')
print(f'O produto dos ímpares é {multimpar}')

22.
notas = []
parciais = 0
reprov = 0
nome = input('Digite seu nome: ')

while True:
    if parciais != 3:
        nota = int(input('Digite sua nota: '))
        if 10 <= nota <= 20:
            notas.append(nota)
            print('nota valida')
            parciais = parciais + 1
        else:
            print('reprovado')
            reprov = reprov + 1
            break
    else:
        break

if reprov == 0:
    print(f'{nome} sua media das notas: {(sum(notas))/3}')
else:
    print(f'{nome} nota muito abaixo do esperado')

23.
valor = []

while True:
    referencia = int(input(f'digite um numero: '))
    for count in range(1, referencia + 1):
        if referencia % count == 0:
            valor.append(count)
    else:
        break
print(valor)

24.
valor = []
while True:
    referencia = int(input(f'digite um numero: '))
    for count in range(1, referencia + 1):
        if referencia % count == 0:
            valor.append(count)
    else:
        break
print(valor)
valor.pop()
print(valor)
print(sum(valor))

25.
valor1 = []
valor2 = []
while True:
    for count in range(1, 1001):
        if count % 3 == 0:
            valor1.append(count)
        if count % 5 == 0:
            valor2.append(count)
    else:
        break
print(valor1)
print(valor2)
print(sum(valor1))
print(sum(valor2))
print(sum(valor1) + sum(valor2))

26.
valor1 = []
valor2 = []
valor3 = []

while True:
    referencia = int(input(f'digite um numero: '))

    for count in range(referencia, 100):
        if count % 11 == 0:
            valor1.append(count)
        if count % 13 == 0:
            valor2.append(count)
        if count % 17 == 0:
            valor3.append(count)
    else:
        break

print(valor1)
print(valor2)
print(valor3)

27.
valor1 = []

while True:
    valor = int(input('Digite um valor: '))
    if valor > 0:
        for count in range(1, valor + 1):
            h = 1 / count
            valor1.append(h)
        else:
            break
    else:
        print('digite um numero positivo')

print(valor1)
print(f'H = {sum(valor1)}')

28.
valor1 = []
valor2 = []
resultado = 1
contador = 1
e = 0

while True:
    valor = int(input('Digite um valor: '))
    if valor > 0:
        for count in range(1, valor + 1):
            while contador <= valor:
                resultado *= contador
                contador += 1
                valor1.append(resultado)
                e = 1 / resultado
                valor2.append(e)
        else:
            break
    else:
        print('digite um numero positivo')

print(valor1)
print(valor2)
print(f'E = {sum(valor2)}')

29.
valor1 = []
valor2 = []
resultado = 1
contador = 1
e = 0
n = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor > 0:
        for count in range(0, 6):
            while contador <= valor:
                resultado *= contador
                contador += 1
                valor1.append(resultado)
                print(n)
                s = n / resultado
                valor2.append(s)
                n = n + 1
        else:
            break
    else:
        print('digite um numero positivo')

print(valor1)
print(valor2)
print(f'S = {sum(valor2)}')

30.
valor1 = []
value = 0
total = 0
while True:
    referencia = int(input(f'digite um numero: '))
    for count in range(1, referencia + 1):
        if count % 2 != 0:
            value = value + 1
            print(f'count: {count}')
            print(f'value: {value}')
            total = count / value
            valor1.append(total)
    else:
        break

print(valor1)
print(f'S = {sum(valor1)}')

31.

"""
import modulo_random

count = 0
n = int(input(f'digite quantas vezes deseja jogar os dados: '))

while n != count:
    d1 = modulo_random.randint(1, 6)
    d2 = modulo_random.randint(1, 6)
    if d1 > d2:
        print(f'Dado 1 ({d1}) maior que Dado 2 ({d2})')
    if d1 < d2:
        print(f'Dado 1 ({d1}) menor que Dado 2 ({d2})')
    else:
        print(f'Dado 1 ({d1}) igual ao Dado 2 ({d2})')
    count = count + 1




