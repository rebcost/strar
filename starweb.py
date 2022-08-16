from credenciais import USERNAME, SENHA
from time import sleep
from partnumber import PartNumber
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


class Starweb:
    # Hidden mode

    options = Options()
    options.headless = False

    # Drive Settings
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    def __init__(self):
        self.acessar_starweb()
        self.loggin()
        sleep(3)
        self.pesquisar_pn()
        self.extrair_tabela()


    def acessar_starweb(self):
        self.driver.get(
            'https://pt.wikipedia.org/w/index.php?title=Especial:Entrar&returnto=Wikip%C3%A9dia%3AP%C3%A1gina+principal')

    def fechar_navegador(self):
        self.driver.close()

    def loggin(self):
        self.driver.find_element(By.XPATH, '//*[@id="wpName1"]').send_keys(USERNAME)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="wpPassword1"]').send_keys(SENHA)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="wpLoginAttempt"]').click()

    def pesquisar_pn(self):
        pn = PartNumber()
        self.driver.find_element(By.XPATH, '//*[@id="searchform"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div/input').send_keys(pn.pn_base())
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button').click()
        sleep(1)

    # def extrair_tabela_html(self):
    #     table = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[9]')
    #     table_html = table.get_attribute('outerHTML')
    #     return table_html

    # def criar_df(self):
    #     # df = pd.read_html(str(self.extrair_tabela_html()))
    #     df = pd.read_html(self.extrair_tabela_html())
    #     print(df)

    def extrair_tabela(self):
        data = []
        # Obtain the number of rows in body
        linhas = 1 + len(self.driver.find_elements(By.XPATH,
                                            '//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr'))

        # Obtain the number of columns in table
        colunas = len(self.driver.find_elements(By.XPATH,
                                        '//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr/th'))
        for c in range(1, colunas + 1):
            for l in range(2, linhas):
                value = self.driver.find_element(By.XPATH,
                                            f"//*[@id='mw-content-text']/div[1]/table[9]/tbody/tr[{str(l)}]/td[{str(c)}]").text
                data.append(value)
        print(data)
        #TODO: Criar um filtro para separar cada tipo de dado


    def converter_csv(self):
        pass
