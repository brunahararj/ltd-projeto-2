import pandas as pd
data = pd.read_csv('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.csv')
print(data.head())
data.to_json('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.json')
json_data = data.to_json()
print(json_data)
with open('/Users/brunahara/Downloads/Projeto-LTD/ltd-projeto-2/documentos/Taco_4a_edicao_2011.json', 'w') as file:
    file.write(json_data)