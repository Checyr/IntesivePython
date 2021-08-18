from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Python39\Scripts\geckodriver.exe', firefox_options=options)
driver.get('http://google.com/')


driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
time.sleep(5)
Dolar = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

driver.get("http://google.com/")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
time.sleep(5)
Euro = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

driver.get("https://www.melhorcambio.com/ouro-hoje")
time.sleep(5)
ouro = driver.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')


#Importando tabela

tabela = pd.read_excel(r"C:\Users\gaby2\Documents\Programação\IntensivaoDePython\Aula 3\selenium\BancoDeDados\Produtos.xlsx")


tabela.loc[tabela["Moeda"] == "Dolár", "Cotação" ] = float(Dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação" ] = float(Euro)
tabela.loc[tabela["Moeda"] == "ouro", "Cotação" ] = float(ouro)

tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Cotação"]
tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Margem"]

tabela["Preço Final"] = tabela["Preço Final"].map("{:.2f}".format)


#exportando a tabela
tabela.to_excel(r"C:\Users\gaby2\Documents\Programação\IntensivaoDePython\Aula 3\selenium\BancoDeDados")