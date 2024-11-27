from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Carregar os dados filtrados do Excel ao iniciar a API
arquivo_excel = "produtos_filtrados.xlsx"
df = pd.read_excel(arquivo_excel)

@app.route('/produtos', methods=['GET'])
def obter_produtos():
    """
    Retorna os produtos filtrados em formato JSON.
    Aceita query parameters opcionais para filtros.
    """
    # Obter parâmetros de filtro (opcionais)
    id_produto = request.args.get('id_produto')
    nome = request.args.get('nome')
    descricao = request.args.get('descricao')
    page = int(request.args.get('page', 1))  # Padrão: 1
    limit = int(request.args.get('limit', 10))  # Padrão: 10

    # Filtrar o DataFrame com base nos parâmetros fornecidos
    df_filtrado = df.copy()
    if id_produto:
        df_filtrado = df_filtrado[df_filtrado['ID_PRODUTO'].astype(str) == id_produto]
    if nome:
        df_filtrado = df_filtrado[df_filtrado['NOME'].str.contains(nome, case=False, na=False)]
    if descricao:
        df_filtrado = df_filtrado[df_filtrado['DESCRICAO'].str.contains(descricao, case=False, na=False)]

    # Implementar paginação
    start = (page - 1) * limit
    end = start + limit
    produtos = df_filtrado[start:end].to_dict(orient='records')

    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)
