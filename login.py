from main import username, password, telegram, user_2, pass_2, user_3, pass_3
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from tkinter import messagebox


def main_con():
 if not username or not password:
     messagebox.showinfo("Erro", "Retorne à página de login e insira suas credenciais.")
     return
 options = uc.ChromeOptions()
 options.headless = True
 options.add_argument('--headless')

 chrome = uc.Chrome(options=options)
 chrome.get('https://www.bet365.com/')  # Abrir Site
 print("Site Aberto...")

 time.sleep(5)  # Esperar 5 segundos para carregar o elemento
 chrome.find_element(
     By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/div').click()
 print("Login principal iniciado...")

 time.sleep(5)  # Esperar 5 segundos para carregar o elemento
 chrome.find_element(
     By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(username)
 chrome.find_element(
     By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(password)
 print("Credenciais inseridas...")

 time.sleep(5)  # Esperar 5 segundos para carregar o elemento
 chrome.find_element(
     By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]').click()
 print("Login Realizado com Sucesso!")

 chrome.quit()

def con_2():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--headless')

    chrome = uc.Chrome(options=options)
    chrome.get('https://www.bet365.com/')  # Abrir Site
    print("Site Aberto...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/div').click()
    print("Login principal iniciado...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(user_2)
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(pass_2)
    print("Credenciais inseridas...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div').click()
    print("Login Realizado com Sucesso!")

    chrome.quit()


def con_3():
    options = uc.ChromeOptions()
    options.headless = True
    options.add_argument('--headless')

    chrome = uc.Chrome(options=options)
    chrome.get('https://www.bet365.com/')  # Abrir Site
    print("Site Aberto...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/div').click()
    print("Login principal iniciado...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(user_3)
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(pass_3)
    print("Credenciais inseridas...")

    time.sleep(5)  # Esperar 5 segundos para carregar o elemento
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div').click()
    print("Login Realizado com Sucesso!")

    chrome.quit()

main_con()