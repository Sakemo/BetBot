import undetected_chromedriver as uc
from undetected_chromedriver import By
import time


def scrap():
    options = uc.ChromeOptions()
    # options.headless=True
    # options.add_argument('--headless')

    chrome = uc.Chrome(options=options)
    chrome.get('https://www.bet365.com/')  # Abrir Site
    chrome.set_window_size(1920, 1080)
    time.sleep(10)

    # Aceitar Cookies
    chrome.find_element(
        By.XPATH, '/html/body/div[3]/div/div[2]/div[2]').click()
    print('Cookies...')

    # Clica em Login
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]').click()
    time.sleep(2)
    print('Login...')

    # Insere usuario
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys('SrMarcondes21')
    time.sleep(2)
    print('Usuario...')

    # Insere senha
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys('220505')
    time.sleep(2)
    print('Senha')

    # Conclui Login
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]').click()
    print('Login com Sucesso')
    time.sleep(5)

    chrome.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div[19]/span').click()
    time.sleep(5)
scrap()
