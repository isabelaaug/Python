"""
Try / Except / Else / Finally

- toda entrada deve ser tratada.

Try - é a ação correta
Except - é a possivel erro
Else - é caso a ação correta sseja executada
Finally - será sempre exeutado


num = 0

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('valor incorreto')

print(f'Voce digitou: {num}')

----------------------

try:
    num = int(input('Informe um numero: '))
    print(f'Voce digitou: {num}')
except ValueError:
    print('valor incorreto')

----------------------

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('valor incorreto')
else:
    print(f'Voce digitou: {num}')

-----------------------

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('valor incorreto')
else:
    print(f'Voce digitou: {num}')
finally:
    print('executando finally')

-----------------------------------

def dividir(a, b):
    return a / b


try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(dividir(num1, num2))

------------------------
# EXCLUSIVO
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:  # ZeroDivisionError: division by zero
        return 'Nao eh possivel'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# GENERICO
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Valor incorreto'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

#SEMI GENERICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Valor incorreto: {erro}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

"""





