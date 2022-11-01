# falta testar e descomentar a linha 141 para aplicar de fato, qualquer coisa ver a versão x3.py

# selenium 4
from os import getenv
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class uniswap:

    def __init__(self, token0: str, 
                 token1: str, 
                 qntd_token0: int, 
                 #preco_Min: int, 
                 #preco_max: int, 
                 quiet: bool = True):
        self.token0 = token0
        self.token1 = token1
        self.qntd_token0 = qntd_token0
        #self.preco_Min = preco_Min
        #self.preco_max = preco_max
        self.quiet = quiet

    # auxiliar functions

    def getSecretPhrase(self):
        load_dotenv()

        return [
                getenv("secretPhrase").split(" "),
                getenv("password")
               ]

    def windowExtension(self):

        chwd = driver.window_handles

        for i in range(len(chwd)):
            driver.switch_to.window(chwd[i])
            t = driver.current_url
            if t.startswith("chrome"):
                break

    def acceptMetamask(self):
        sleep(5)
        self.windowExtension()


        sleep(2)
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-primary").click()
        driver.find_element(by=By.CSS_SELECTOR, value=".btn-primary").click()



    def checkToken(self, token):

        elemento= driver.find_element(by=By.XPATH, value='/html/body/reach-portal[2]/div[3]/div/div/div/div/div[3]/div[1]/div/div/div[1]')

        if elemento.get_attribute('disabled') == 'true':
            print('token já selecionado')
            driver.find_element(by=By.CSS_SELECTOR, value='.hCDFrE').click()
        else:
            if elemento.text.split("\n")[1] == token:
                elemento.click()

    def writePoolId(self,poolId):
        open('poolId.txt','w').write(poolId)

    # main functions


    def initSel(self):
        global driver
        chop = webdriver.ChromeOptions()
        chop.add_extension('../extensions/metamask.crx')
        chop.add_argument('auto-open-devtools-for-tabs')
        if self.quiet:
            chop.add_argument('--headless=chrome')
            chop.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chop)
        driver.implicitly_wait(10)
        print("\nchrome Iniciado")
        return driver

    def metamask(self):
        chwd = driver.window_handles
        driver.switch_to.window(chwd[0])

        driver.find_element(by=By.CSS_SELECTOR, value=".button").click()
        driver.find_element(
            by=By.CSS_SELECTOR, value="[data-testid=page-container-footer-next]").click()
        driver.find_element(by=By.CSS_SELECTOR,
                            value="[data-testid=import-wallet-button]").click()

        secretPhrase, password = self.getSecretPhrase()  # desestruturação
        # senha de 12 palavras
        for i in range(12):
            driver.find_element(
                by=By.CSS_SELECTOR, value=f"[data-testid=import-srp__srp-word-{i}]").send_keys(secretPhrase[i])

        driver.find_element(by=By.ID, value="password").send_keys(password)
        driver.find_element(
            by=By.ID, value="confirm-password").send_keys(password)
        driver.find_element(
            by=By.ID, value="create-new-vault__terms-checkbox").click()
        driver.find_element(by=By.CSS_SELECTOR,
                            value=".create-new-vault__submit-button").click()
        sleep(5)
        driver.find_element(by=By.CSS_SELECTOR,
                            value="[data-testid=EOF-complete-button]").click()


        driver.close()  # fecha a aba
        driver.switch_to.window(driver.window_handles[0])
        print("metamask configurada")

    def connectWallet(self):
        driver.get("https://app.uniswap.org/#/swap")
        sleep(2)
        driver.find_element(
            by=By.CSS_SELECTOR, value="[data-testid=navbar-connect-wallet]").click()
        driver.find_element(by=By.ID, value="metamask").click()

        self.acceptMetamask()
        print("Carteira conectada a uniswap")

    def redePolygon(self):
        sleep(2)
        chwd = driver.window_handles
        driver.switch_to.window(chwd[0])
        driver.find_element(
            by=By.XPATH, value='//*[@id="root"]/div/div[1]/nav/div/div[1]/div[1]/div/button').click()
        driver.find_elements(by=By.CSS_SELECTOR,
                             value=".sc-ocqcjd-1")[1].click()

        self.acceptMetamask()

        driver.switch_to.window(chwd[0])
        print("alterado da rede da ethereum pra polygon")


    def creatingPool(self):
        driver.get("https://app.uniswap.org/#/pool")
        driver.find_element(by=By.ID, value="join-pool-button").click()


        # botoes token

        elemento_Btn= driver.find_elements(by=By.CSS_SELECTOR, value=".token-symbol-container")


        # selecionando token primario
        elemento_Btn[0].click()
        driver.find_element(
            by=By.ID, value="token-search-input").send_keys(self.token0)
        sleep(2)
        self.checkToken(self.token0)

        # selecionando token secundario
        elemento_Btn[1].click()
        driver.find_element(
            by=By.ID, value="token-search-input").send_keys(self.token1)
        sleep(2)
        self.checkToken(self.token1)

        # inserindo a quantidade de token0
        sleep(2)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        driver.find_element(
            by=By.CSS_SELECTOR, value=".token-amount-input").send_keys(self.qntd_token0)


        elementos= driver.find_elements(by=By.CSS_SELECTOR, value=".rate-input-0")



        '''
        for i in range(len(elementos)):
            if i == 1:
                driver.execute_script(f"document.querySelectorAll('.rate-input-0')[0].value={preco_Min}")
            else:
                driver.execute_script(f"document.querySelectorAll('.rate-input-0')[1].value={preco_max}")


        driver.find_element(by=By.CSS_SELECTOR,value=".sc-dphd4z-11").click()
        '''
        print("Pool Criada")
        sleep(5)


    def main(self):

        self.initSel()
        self.metamask()
        self.connectWallet()
        self.redePolygon()
        self.creatingPool()
        driver.close()




f= uniswap(token0 = "MATIC", token1 = "AAVE", qntd_token0=10, quiet=True)
f.main()
