##falta testar e descomentar a linha 141 para aplicar de fato, qualquer coisa ver a versão x3.py

# selenium 4
import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

def initSel():
    chop = webdriver.ChromeOptions()
    chop.add_extension('extension_10_20_0_0.crx')
    chop.add_argument('auto-open-devtools-for-tabs')
    chop.add_argument('--headless=chrome')
    driver = webdriver.Chrome(chrome_options = chop)
    driver.implicitly_wait(10)
    return driver


#configurando a metamask
def metamask():
    chwd = driver.window_handles
    driver.switch_to.window(chwd[0])

    driver.find_element(by=By.CSS_SELECTOR,value=".button").click()
    driver.find_element(by=By.CSS_SELECTOR,value="[data-testid=page-container-footer-next]").click()
    driver.find_element(by=By.CSS_SELECTOR,value="[data-testid=import-wallet-button]").click()

    #senha de 12 palavras
    for i in range(12):
        driver.find_element(by=By.CSS_SELECTOR,value=f"[data-testid=import-srp__srp-word-{i}]").send_keys(mySecretPhrase[i])

    driver.find_element(by=By.ID,value="password").send_keys("3Fd445ab@")
    driver.find_element(by=By.ID,value="confirm-password").send_keys("3Fd445ab@")
    driver.find_element(by=By.ID,value="create-new-vault__terms-checkbox").click()
    driver.find_element(by=By.CSS_SELECTOR,value=".create-new-vault__submit-button").click()
    sleep(5)
    driver.find_element(by=By.CSS_SELECTOR,value="[data-testid=EOF-complete-button]").click()


    driver.close() # fecha a aba
    driver.switch_to.window(driver.window_handles[0])

#conectando carteira a uniswap

def connectWallet():
    driver.get("https://app.uniswap.org/#/swap")
    sleep(2)
    driver.find_element(by=By.CSS_SELECTOR,value="[data-testid=navbar-connect-wallet]").click()
    driver.find_element(by=By.ID,value="metamask").click()

    sleep(5)
    chwd = driver.window_handles


    for i in range(len(chwd)):
        driver.switch_to.window(chwd[i])
        t = driver.current_url
        if t.startswith("chrome"):
            break


    sleep(2)
    driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()
    driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()


# mudando pra rede da polygon

def redePolygon():
    sleep(2)
    chwd = driver.window_handles
    driver.switch_to.window(chwd[0])
    driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/nav/div/div[1]/div[1]/div/button').click()
    driver.find_elements(by=By.CSS_SELECTOR,value=".sc-ocqcjd-1")[1].click()
    sleep(5)
    chwd = driver.window_handles

    for i in range(len(chwd)):
        driver.switch_to.window(chwd[i])
        t = driver.current_url
        if t.startswith("chrome"):
            break

    driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()
    driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()

    driver.switch_to.window(chwd[0])

#Criando pool

def creatingPool():
    driver.get("https://app.uniswap.org/#/pool")
    driver.find_element(by=By.ID,value="join-pool-button").click()


    #botoes token

    elemento_Btn = driver.find_elements(by=By.CSS_SELECTOR,value=".token-symbol-container")


    # selecionando token primario
    elemento_Btn[0].click()
    driver.find_element(by=By.ID,value="token-search-input").send_keys(token0)
    sleep(2)
    elemento = driver.find_element(by=By.CSS_SELECTOR,value=".css-1j6a53a ")

    if elemento.text == token0:
        elemento.click()

    # selecionando token secundario
    elemento_Btn[1].click()
    driver.find_element(by=By.ID,value="token-search-input").send_keys(token1)
    sleep(2)
    elemento = driver.find_element(by=By.CSS_SELECTOR,value=".css-1j6a53a ")

    if elemento.text == token1:
        elemento.click()

    # inserindo a quantidade de token0
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(by=By.CSS_SELECTOR,value=".token-amount-input").send_keys(qntd_token0)


    elementos = driver.find_elements(by=By.CSS_SELECTOR,value=".rate-input-0")



    '''
    for i in range(len(elementos)):
        if i == 1:
            driver.execute_script(f"document.querySelectorAll('.rate-input-0')[0].value={preco_Min}")
        else:
            driver.execute_script(f"document.querySelectorAll('.rate-input-0')[1].value={preco_max}")


    driver.find_element(by=By.CSS_SELECTOR,value=".sc-dphd4z-11").click()
    '''





# moeda principal e moeda secundaria

token0 = "WETH"
token1 = "AAVE"
qntd_token0 = 10
preco_Min = 0
preco_max = 0.1

#Importando a palavra secreta pro python
load_dotenv()
mySecretPhrase = os.getenv("secretPhrase").split(" ")

#Iniciando webdriver

driver = initSel()
print("chrome Iniciado\n")
metamask()
print("metamask configurada\n")
connectWallet()
print("Carteira conectada a uniswap\n")
redePolygon()
print("alterado da rede da ethereum pra polygon\n")
creatingPool()
print("Pool Criada\n")
driver.close()
