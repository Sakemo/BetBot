from flask import Flask, render_template, request, jsonify, redirect, url_for
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from tkinter import messagebox
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
import pandas as pd
import numpy as np

app = Flask(__name__)

username = ""
password = ""
telegram = ""
user_2 = ""
pass_2 = ""
user_3 = ""
pass_3 = ""
martingale = ""
stopwin = ""
stoploss = ""
value = ""

tableData=[]
league1 = ""
league2 = ""
league3 = ""
league4 = ""

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/config')
def config():
    return render_template('config.html')


@app.route('/bot')
def bot():
    return render_template('analise.html')

@app.route('/bot/aposta', methods=['POST'])
def bot_config():
    tableData = request.form['array']
    league1 = request.form['league1']
    league2 = request.form['league2']
    league3 = request.form['league3']
    league4 = request.form['league4']

    print(tableData)
    print(league1)
    print(league2)
    print(league3)
    print(league4)
    redirect(url_for('bot'))
    return jsonify({'success': True})

@app.route('/bot/config', methods=['POST'])
def config_bot():
    martingale = request.form['martingale']
    stopwin = request.form['stopwin']
    stoploss = request.form['stoploss']
    value = request.form['valor']

    print(martingale)
    print(stopwin)
    print(stoploss)
    print(value)

    redirect(url_for('config'))
    return jsonify({'success': True})


@app.route('/login/conect', methods=['POST'])
def conect():
    username = request.form['username']
    password = request.form['password']
    telegram = request.form['telegram']
    print(username)
    print(password)
    print(telegram)
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

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(username)
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(password)
    print("Credenciais inseridas...")

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div').click()
    print("Login Realizado com Sucesso!")
    time.sleep(5)  # Esperar 5 segundos para carregar o elemento

    chrome.quit()

    redirect(url_for('login'))
    return jsonify({'success': True})

# Rota para lidar com a solicitação AJAX de conect_2()


@app.route('/login/conect_2', methods=['POST'])
def conect_2():
    user_2 = request.form['user_2']
    pass_2 = request.form['pass_2']
    print(user_2)
    print(pass_2)
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

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(user_2)
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(pass_2)
    print("Credenciais inseridas...")

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div').click()
    print("Login Realizado com Sucesso!")
    time.sleep(5)  # Esperar 5 segundos para carregar o elemento

    chrome.quit()

    redirect(url_for('login'))
    return jsonify({'success': True})

# Rota para lidar com a solicitação AJAX de conect_3()


@app.route('/login/conect_3', methods=['POST'])
def conect_3():
    user_3 = request.form['user_3']
    pass_3 = request.form['pass_3']
    print(user_3)
    print(pass_3)

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

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input').send_keys(user_3)
    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input').send_keys(pass_3)
    print("Credenciais inseridas...")

    chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div').click()
    print("Login Realizado com Sucesso!")
    time.sleep(5)  # Esperar 5 segundos para carregar o elemento

    chrome.quit()

    redirect(url_for('login'))
    return jsonify({'success': True})


# Colocara o site no ar
if __name__ == "__main__":
    app.run(debug=True)
