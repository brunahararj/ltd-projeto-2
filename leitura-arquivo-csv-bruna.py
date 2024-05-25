import pandas as pd
tabela_taco = pd.read_csv('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.csv')
print(tabela_taco)
tabela_taco.to_json('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.json')
json_tabela_taco = tabela_taco.to_json()
print(json_tabela_taco)
with open('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.json', 'w') as file:
    file.write(json_tabela_taco)
