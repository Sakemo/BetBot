import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
import pandas as pd
import numpy as np

#Mostra as opções para o usuário escolher
print("[1]Copa do Mundo")
print("[2]Euro Cup")
print("[3]Premier League")
print("[4]Super League")
print("[5]Super Liga Sul-Americana")

# Obtém a escolha do usuário
escolha = input("Escolha a liga desejada: ")

# Verifica qual opção foi escolhida e define a variável league
if escolha == "1":
    league = "Copa do Mundo"
elif escolha == "2":
    league = "Euro Cup"
elif escolha == "3":
    league = "Premier League"
elif escolha == "4":
    league = "Super League"
elif escolha == "5":
    league = "Super Liga Sul-Americana"
else:
    print("Opção inválida.")
    exit()

# Imprime a liga escolhida
print("Campeonato de analise:", league)

data = date.today() - timedelta(days=1)
dia = data.strftime("%a %b %d %Y")

print("Data de Analise:", dia)


def scrapper():
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')

    chrome = uc.Chrome(options=options)
    chrome.get('https://extra.bet365.com/results/br') #Abrir Site
    chrome.set_window_size(1920,108    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')

    chrome = uc.Chrome(options=options)
    chrome.get('https://extra.bet365.com/results/br') #Abrir Site
    chrome.set_window_size(1920,1080)

    chrome.find_element(By.XPATH, '/html/body/div/div[4]/div/div[2]/div/div[2]/div[2]/div').click() # Aceitar Cookies
    time.sleep(1)

    # Abre Login
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div[3]/div/div/div[2]/a/div').click()
    time.sleep(1)
    print('Conectando...')

    # Coloca Nome de Usuario
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[1]/input[2]').click()
    time.sleep(1)
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[1]/input[2]').send_keys("SrMarcondes21")
    print('Inserindo credenciais...')

    # Coloca Senha
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/input[2]').click()
    time.sleep(1)
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[2]/input[2]').send_keys("220505")

    # Realiza Login
    chrome.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/a').click()
    print('Concedendo tempo de espera...')
    chrome.set_page_load_timeout(60)
    time.sleep(6)
    print('Tempo de espera concedido!')

    # Abre banco de dados de resultados de partidas
    chrome.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/main/div[4]/div[1]/button').click()
    print('Acessando banco de dados...')
    time.sleep(3)

    # Especifica 'Futebol Virtual'
    chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/input').click()
    chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/input').send_keys("Futebol Virtual")
    time.sleep(3)
    chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[57]/button').click()
    time.sleep(3)
    print('Banco de dados acessado!')

    # Definindo tempo de analise
    chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/button[1]').click()
    time.sleep(3)
    print("Definindo tempo de analise...")
    chrome.find_element(By.CSS_SELECTOR, f'[aria-label="{dia}"]').click()
    time.sleep(1)
    chrome.find_element(By.CSS_SELECTOR, f'[aria-label="{dia}"]').click()
    time.sleep(1)
    chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/button').click()
    time.sleep(1)
    print('Tempo de analise definido')

    # Definindo campeonato
    print(f'Buscando resultados para {league} no tempo {dia}')
    if league == "Copa do Mundo":
        chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/div/div[3]/button').click()
    elif league == "Euro Cup":
        chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/div/div[4]/button').click()
    elif league == "Premier League":
        chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/div/div[5]/button').click()
    elif league == "Super League":
        chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/div/div[6]/button').click()
    elif league == "Super Liga Sul-Americana":
        chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/div/div[7]/button').click()
    else:
        print("Liga Invalida, por favor reinicie.")

    print("Iterando Campeonato...")

    # Cria lista com todos os jogos da data selecionada
    time.sleep(2)
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    num_lst = list(range(1, len(numeros)+1))
    lst_2 = len(num_lst)
    ###################################################
    jogos = chrome.find_elements(By.CLASS_NAME, "point-result__fixture") # Encontra os botões dos jogos
    lst = list(range(1, len(jogos)+1))
    rst_lst = []
    score_lst=[]
    num = len(lst) # Define a quantidade de jogos no dia
    ###################################################
    for i in range(1, num +1):
        xpath = f"/html/body/div[1]/div[2]/div[2]/main/div[4]/div[3]/div/button[{i}]"
        print(len(xpath))
        xpaths = chrome.find_elements(By.XPATH, xpath)
        print("Etapa 1")
        for xpath in xpaths:
            xpath.click() # Abre os resultados de cada jogo
            print("Etapa 2")
            time.sleep(2)
            for i in range(1, lst_2+1):
                chrome.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/main/div[4]/div[4]/div/div[8]/div[4]/div[{i}]/button').click() # Clica nas apostas
                time.sleep(2)
                result = chrome.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/main/div[4]/div[4]/div/div[8]/div[4]/div[{i}]/div/div[3]/div[1]/div[1]') # Copia os resultados
                rst = result.text
                rst_lst.append(rst) # Armazena restultados para uso posterior
            for i in range(4, len(rst_lst), 5):
                score_lst.append(rst_lst[i])

            chrome.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/main/div[3]/div/div/button').click() # Retorna a lista de jogos
            print("Etapa 3")
            time.sleep(1)
    # Criando Tabela
    chrome.quit()
    print("Analise Finalizada com Sucesso!")

scrapper()

