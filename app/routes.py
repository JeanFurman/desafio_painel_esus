from flask import jsonify, request
from app import app
from app.utils import abrir_arquivo

import re

@app.route('/api/v1/atendimentos', methods=['GET'])
def get_atendimentos():

    dados = abrir_arquivo()

    params = request.args

    data_atendimento = params.get('data_atendimento')
    if data_atendimento:
        formato_data = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        if not formato_data.match(data_atendimento):
            return jsonify({'error': f'Formato invalido para data. Use YYYY-mm-dd.'}), 400

    # Caso queira todos os parametros do csv
    params_corretos = dict(filter(lambda item: item[0] in dados[0], params.items()))
    
    # Apenas os parametros pedidos no git
    # params_git = ["data_atendimento", "condicao_saude", "unidade"]
    # params_corretos = dict(filter(lambda item: item[0] in params_git, params.items())) 

    for chave, valor in params_corretos.items():
        dados = [p for p in dados if p[chave] == valor]

    return jsonify({'atendimentos': dados})