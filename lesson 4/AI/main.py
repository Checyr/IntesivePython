import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#inteligencia artificial
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

tabela = pd.read_csv(r"C:\Users\gaby2\Documents\Programação\IntensivaoDePython\Aula 4\InteligenciaArtificial\BancoDeDados\advertising.csv")

sns.heatmap(tabela.corr())

#separar dados de x e de y]

#y e quem eu quero descobrir
y = tabela["Vendas"]
#x e o resto
x = tabela.drop("Vendas", axis = 1)#0 = linha 1 = coluna

#aplicar o train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y)# tem que ser nessa ordem x_treino x_teste y_treino y_teste
#passar quanto ele tem que treinar e quanto de test traind_test_split(x,y test_size =0.3) 0.3 de 30 porcento

modelo_regressaolinear = LinearRegression()
modelo_randomforest = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_randomforest.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_randomforest = modelo_randomforest.predict(x_teste)

#Teste de Inteligencia Artificial E melhor modelo

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_randomforest))

#visualização Grafica das Previsoes
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_test"] = y_teste
tabela_auxiliar["regressao linear"] = previsao_regressaolinear
tabela_auxiliar["random forest"] = previsao_randomforest

plt.figure(figsize=(15, 6))
sns.lineplot(data=tabela_auxiliar)
plt.show()