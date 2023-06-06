from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd


class Web:
    def __init__(self):
        self.site = 'https://projetosemds.com.br/manuela/'

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()
        self.apple()
        self.samsung()
        self.motorola()
        self.planilha()

        self.apple_preco = None
        self.apple_modelo = None

        self.samsung_preco = None
        self.samsung_modelo = None

        self.motorola_preco = None
        self.motorola_modelo = None

    def abrir_site(self):
        self.driver.get(self.site)
        sleep(5)

    def apple(self):
        print('\n\n-----> Apple')

        self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]/a').click()

        self.apple_modelo = []
        self.apple_preco = []

        for i in range(5):
            modelo = self.driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div[{i + 1}]/text/p').text
            preco = self.driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div[{i + 1}]/text/h3').text

            dados = [modelo, preco]
            print(dados)

            self.apple_modelo.append(modelo)
            self.apple_preco.append(preco)

    def samsung(self):
        print('\n\n-----> SAMSUNG')

        self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]/a').click()

        self.samsung_modelo = []
        self.samsung_preco = []

        for i in range(5):
            modelo = self.driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div[{i + 1}]/text/p').text
            preco = self.driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div[{i + 1}]/text/h3').text

            dados = [modelo, preco]
            print(dados)

            self.samsung_modelo.append(modelo)
            self.samsung_preco.append(preco)

    def motorola(self):
        print('\n\n-----> MOTOROLA')

        self.driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]/a').click()

        self.motorola_preco = []
        self.motorola_modelo = []

        for i in range(5):
            modelo = self.driver.find_element(By.XPATH, f'/html/body/div/div[5]/div/div[{i + 1}]/text/p').text
            preco = self.driver.find_element(By.XPATH, f'/html/body/div/div[5]/div/div[{i + 1}]/text/h3').text

            dados = [modelo, preco]
            print(dados)

            self.motorola_modelo.append(modelo)
            self.motorola_preco.append(preco)

    def planilha(self):
        global dispositivos
        d_modelo = [self.apple_modelo, self.samsung_modelo, self.motorola_modelo]
        d_preco = [self.apple_preco, self.samsung_preco, self.motorola_preco]
        # for i in range(5):

        dispositivos = {'Modelo': self.apple_modelo, 'Preço': self.apple_preco}
        dispositivos = {'Modelo': self.samsung_modelo, 'Preço': self.samsung_preco}
        dispositivos = {'Modelo': self.motorola_modelo, 'Preço': self.motorola_preco}

        print(dispositivos)
        dados = pd.DataFrame(data=dispositivos)
        print("Dados", dados)
        dados.to_excel('projeto_magazu.xlsx')
