import pandas as pd

# Nome do arquivo Excel gerado anteriormente
arquivo_excel = "produtos_abcfarma_completo.xlsx"

# Carregar o Excel em um DataFrame
df = pd.read_excel(arquivo_excel)

# Selecionar apenas as colunas desejadas
colunas_desejadas = [
    "ID_PRODUTO", 
    "NOME", 
    "DESCRICAO", 
    "COMPOSICAO", 
    "PF_22", 
    "PMC_22", 
    "NOVO", 
    "PRODUTO_REFERENCIA", 
    "NOME_FABRICANTE", 
    "ID_TIPO_PRODUTO", 
    "DESCRICAO_TIPO_PRODUTO"
]

# Filtrar as colunas no DataFrame
df_filtrado = df[colunas_desejadas]

# Salvar o DataFrame filtrado em um novo arquivo Excel
df_filtrado.to_excel("produtos_filtrados.xlsx", index=False)

print("Dados filtrados salvos em 'produtos_filtrados.xlsx'")
