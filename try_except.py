"""
O bloco Try/Except

-usamos para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar
e o usuário recebe mensagens de erros inesperadas.

try:
    geek()
except:  # tratando de maneira generica, sem dizer o tipo
    print('Deu erro')

----------------------------

try:
    len(5)
except TypeError as err:
    print(f'O app gerou o seguinte erro: {err}')  # O app gerou o seguinte erro: object of type 'int' has no len()

--------------------------

try:
    len(5)
except TypeError as err:
    print(f'O app gerou o seguinte erro: {err}')  # O app gerou o seguinte erro: object of type 'int' has no len()

----------------------------

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'geek'}
print(pega_valor(dic, 'game'))
print(pega_valor(dic, 'nome'))
print(pega_valor(5, 'nome'))

"""




