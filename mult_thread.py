import time
from threading import Thread

contador = 5000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start()  # inicia Tempo em segundos: 0.8769242763519287 0.8564009666442871 0.6142289638519287
t2.start()
t1.join()  # executa
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
