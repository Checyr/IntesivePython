import os
import pyautogui
import pyperclip
import time
import pandas as pd

#abrir o navegador
os.startfile(r'C:\\Users\\gaby2\AppData\\Local\\Programs\\Opera GX\\launcher.exe')#r para ignorar os \u que são comandos do python

pyautogui.PAUSE = 1

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

pyperclip.copy(link)
time.sleep(5)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('ctrl')

time.sleep(5)

pyautogui.click(x=491, y=372, clicks=2) 

pyautogui.click(x=491, y=372)

pyautogui.click(x=491, y=372, button="right")

pyautogui.click(x=583, y=862,)

tabela = pd.read_excel(r"C:\Users\gaby2\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(tabela)

pyautogui.hotkey("ctrl", "t")
link2 = "https://mail.google.com/mail/u/0/"
pyperclip.copy(link2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=86, y=198)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.write("Relatorio de venda")
pyautogui.press("tab")
texto = f"""Prezados, Bom dia
o faturamento foi de {faturamento:,.2f}
a quantidade foi de {quantidade:,.2f}

abs,
Gabrielly
"""
pyautogui.write(texto)

pyautogui.hotkey("ctrl", "enter")