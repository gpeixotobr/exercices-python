import pyautogui
import pyperclip
import time
import pandas as pd

'''
Objetivo: realizar uma automação de sistemas e processos

step_1: acessar o sistema
step_02: navegar no sistema até encontrar a base de dados
step_03: exportar a base de dados as
step_04: calcular os indicadores necessários
setp_05: enviar um email com os indicadores'''

#início do código
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=1055, y=504)
time.sleep(3)
pyautogui.click(x=127, y=133)
time.sleep(2)
pyperclip.copy('paloma.carolinen@gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
time.sleep(1)
pyperclip.copy('Relatório atualizado')
pyautogui.hotkey('ctrl','v')
time.sleep(2)
pyautogui.press('tab')
time.sleep(1) 
texto = r'''Prezado. Este é um email automatizado gerado para a produção de um eventual relatório que venha a ser produzido no futuro.
Neste relatório devem conter dados importantes e atualizados para eventuais análises e posteriores tomadas de decisão.
Portanto, seguem as informações abaixo.

Atenciosamente, Python.'''
pyperclip.copy(texto)
time.sleep(2)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('ctrl','enter')
#fim do código