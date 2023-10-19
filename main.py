from tkinter import Tk, filedialog
import pyautogui
from selenium.webdriver.common.by import By

caminho_arquivo = filedialog.askopenfilename(title="Escolha a imagem de referência")

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

frase = ""
primeiro = True

grupos = []

for linha in linhas:
    if primeiro == True:
        frase = frase + linha
        frase = frase.replace("{", "")
        frase = frase.replace("}", "")
        #frase = frase.replace('\n', '\\n')

        if "}\n" in linha:
            primeiro = False
        else:
            primeiro = True
    else:
        grupos.append(linha)


from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()


driver.get('https://web.whatsapp.com/')

input("Aperte enter após ler")

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")

searchBox = driver.find_element(By.CLASS_NAME, '_2vDPL')

searchBox.click()

for grupo in grupos:
    time.sleep(3)
    pyautogui.write(grupo)
    time.sleep(0.5)
    result = driver.find_element(By.CLASS_NAME, '_8nE1Y')
    result.click()
    time.sleep(0.5)
    pyautogui.write(frase)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    searchBox = driver.find_element(By.CLASS_NAME, '_2vDPL')
    searchBox.click()

input('Pressione qualquer tecla para encerrar...')