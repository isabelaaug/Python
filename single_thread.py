import time
from threading import Thread

contador = 5000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')  # Tempo em segundos: 0.8769242763519287 0.8564009666442871
