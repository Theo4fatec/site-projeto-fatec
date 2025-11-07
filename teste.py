from datetime import datetime
import pandas as pd
from colab.models import EGA_KPIS_PROD

format_cod = '%d/%m/%y %H:%M:%S'

df_EGA_KPIS_PROD = pd.read_csv('EGA_KPIS_PROD.csv', sep = ';')

model_instances = []
for row_data in df_EGA_KPIS_PROD.to_dict('records'):
    instance = EGA_KPIS_PROD(
        recid = row_data['RECID'],
        maquina = row_data['MAQUINA'],
        registro = datetime.strptime (row_data['REGISTRO'], format_cod),
        os = row_data['OS'],
        produto = row_data['PRODUTO'],
        operacao = row_data['OPERACAO'],
        molde = row_data['MOLDE'],
        ttotal = row_data['TTOTAL'],
        sec_total = row_data['SEC_TOTAL'],
        tdisp = row_data['TDISP'],
        sec_disp = row_data['SEC_DISP'],
        tprod = row_data['TPROD'],
        sec_prod = row_data['SEC_PROD'],
        qtde_std = row_data['QTDE_STD'],
        qtde_real = row_data['QTDE_REAL'],
        qtde_boas = row_data['QTDE_BOAS'],
        teep = row_data['TEEP'],
        oee = row_data['OEE'],
        disp = row_data['DISP'],
        perf = row_data['PERF'],
        qualidade = row_data['QUALIDADE'],
        )
    model_instances.append(instance)


EGA_KPIS_PROD.objects.bulk_create(model_instances)






















#exemplo inicial
format_cod = '%d/%m/%Y %H:%M'
teste = EGA_KPIS_PROD(
recid = 28,
maquina = 1,
registro = datetime.strptime ('25/04/2025 10:19', format_cod),
os = 45781,
produto = 1361,
operacao = 0,
molde = 201,
ttotal = 5883888,
sec_total = 21182,
tdisp = 5883888,
sec_disp = 21182,
tprod = 5671388,
sec_prod = 20417,
qtde_std = 537,
qtde_real = 310,
qtde_boas = 247,
teep = 4434,
oee = 4434,
disp = 9639,
perf = 5773,
qualidade = 7968)