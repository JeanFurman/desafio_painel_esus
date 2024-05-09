import csv
from datetime import datetime

def formatar_datas_csv(data):
    formatos = ['%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d', '%d %B, %Y']
    for f in formatos:
        try:
            dt = datetime.strptime(data, f)
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            pass

dados = None

def abrir_arquivo():
    global dados
    dados = []
    with open('atendimentos.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for r in leitor_csv:
            nr = {}
            for chave, valor in r.items():
                if chave == 'data_atendimento':
                    nr[chave] = formatar_datas_csv(valor)
                    continue
                nr[chave.lower()] = valor
            dados.append(nr)

def get_dados():
    return dados