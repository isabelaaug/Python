def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente so vive uma vez'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Dormi demais!'
    else:
        return f'Continuo cansado so dormi {num_horas} horas'


def engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

