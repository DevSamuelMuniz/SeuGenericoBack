import requests
import pandas as pd

url = "https://webserviceabcfarma.org.br/webservice/"
cnpj_cpf = "24392409000169"
senha = "SincofarmaAbcfarma@2024"
cnpj_sh = "24392409000169"

dados_total = []

total_paginas = 19

for pagina in range(1, total_paginas + 1):
    payload = {
        "cnpj_cpf": cnpj_cpf,
        "senha": senha,
        "cnpj_sh": cnpj_sh,
        "pagina": pagina
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        
        dados_total.extend(data.get("data", []))
        print(f"Página {pagina} processada com sucesso.")
    else:
        print(f"Erro ao processar a página {pagina}: {response.status_code} - {response.text}")
        break

if dados_total:
    df = pd.DataFrame(dados_total)
    df.to_excel("produtos_abcfarma_completo.xlsx", index=False)
    print("Dados salvos com sucesso em 'produtos_abcfarma_completo.xlsx'")
else:
    print("Nenhum dado foi obtido da API.")