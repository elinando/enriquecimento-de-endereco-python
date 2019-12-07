import pycep_correios
import pandas as pd


#buscando dados do CEP usando biblioteca pycep_correios
endereco = pycep_correios.consultar_cep('07242150')

#atribuindo os dados  retornados pela consulta a variaveis(somente os dado que preciso 
a= endereco['end']
b= endereco['bairro']
c= endereco['cidade']
d= endereco['uf']

#criando um data frame com as variaveis que receberam os dados
res3 = pd.DataFrame({'LOGRADOURO': [a],
                     'BAIRRO': [b],
                     'CIDADE': [c],
                     'UF': [d]})


#adicionando uma coluna de REGIAO, construida pela lógica a baixo
def uf_regiao(row):
    if row["UF"] == "SP":
        return "SUDESTE"
    else:
        return "OUTROS"

res3 = res3.assign(REGIAO=res3.apply(uf_regiao, axis=1))


# gerando um arquivo xls com o data frame final
res3.to_excel("output.xlsx", sheet_name='Sheet_name_1')

print(res3)
