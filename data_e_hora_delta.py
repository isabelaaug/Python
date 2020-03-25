"""
Trabalhando com Deltas (data_final - data_inicial) de Data e Hora

import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2020, 4, 20, 0)
tempo_para_evento = aniversario - data_hoje
print(repr(tempo_para_evento))
print(tempo_para_evento)
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60}h para o aniversario!')


"""
import datetime

data_compra = datetime.datetime.now(verbose_name='Data de Criacao')
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento = data_compra + regra_boleto
print(f'Vencimento {vencimento}')

