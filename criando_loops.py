"""
Criando sua pripria versao de loops

for num in [1, 3, 4, 8]:
    print(num)  # 1, 3, 4, 8


"""


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('isabela')

