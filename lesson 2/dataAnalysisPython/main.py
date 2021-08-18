import pandas as pd
import plotly.express as px
import time
import plotly.offline

tabela = pd.read_csv(r"C:\Users\gaby2\Documents\Programação\IntensivaoDePython\Aula 2\AnaliseDeDadosPython\BancoDeDados\telecom_users.csv")

#excluindo coluna
tabela = tabela.drop("Unnamed: 0", axis=1) # axis linha = 0  coluna = 1

#Sempre que importar uma base de dados verifique como o python ve aquele banco de dados
print(tabela.info())

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")#errors  se ele vai ignorar as caixas em branco corce faz com que ele ignore

#all Excluir colunas COMPLETAMENTE vazias
#any excluir colunas com PELO MENOS 1 valor vazio
tabela = tabela.dropna(how="all", axis=1)#how = como ele vai olhar os valores vazios existe 2 opção any e all 

tabela = tabela.dropna(how="any", axis=0)

print(tabela['Churn'].value_counts)
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))

index = 0
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    plotly.offline.plot(grafico, filename=f'{coluna}.html')


