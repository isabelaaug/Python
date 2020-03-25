import time
from multiprocessing import Pool

contador = 5000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=4)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador // 2])
    r2 = pool.apply_async(contagem_regressiva, [contador // 2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos: {fim - inicio}')
    # Tempo em segundos: 0.8769242763519287 0.8564009666442871 0.6142289638519287


