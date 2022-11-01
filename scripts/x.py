# selenium 4
import os
from dotenv import load_dotenv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 


# moeda principal e moeda secundaria

token0 = "MATIC"
token1 = "AAVE"
qntd_token0 = 10
preco_Min = 0
preco_max = 0.1

#Importando a palavra secreta pro python
load_dotenv()
mySecretPhrase = os.getenv("secretPhrase").split(" ")

#Iniciando webdriver

chop = webdriver.ChromeOptions()
chop.add_extension('extension_10_20_0_0.crx')
#chop.add_argument('auto-open-devtools-for-tabs')
driver = webdriver.Chrome(chrome_options = chop)


#configurando a metamask
chwd = driver.window_handles
driver.switch_to.window(chwd[0])
driver.current_url

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

# configurando a uniswap
driver.get("https://app.uniswap.org/#/swap")
sleep(2)
driver.find_element(by=By.CSS_SELECTOR,value="[data-testid=navbar-connect-wallet]").click()
driver.find_element(by=By.ID,value="metamask").click()

sleep(2)
chwd = driver.window_handles
driver.switch_to.window(chwd[1])
sleep(2)
driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()
driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()
sleep(2)
driver.switch_to.window(chwd[0])

# mudando da rede da ethereum pra polygon

driver.execute_script('document.querySelector(".rgw6ez4l4").click()')
driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/nav/div/div[1]/div[1]/div/button')
driver.find_elements(by=By.CSS_SELECTOR,value=".sc-ocqcjd-1")[1].click()
chwd = driver.window_handles

driver.switch_to.window(chwd[1])
driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()
driver.find_element(by=By.CSS_SELECTOR,value=".btn-primary").click()

driver.switch_to.window(chwd[0])

#Criando pool

driver.get("https://app.uniswap.org/#/pool")
driver.find_element(by=By.ID,value="join-pool-button").click()


#botoes token

elemento_Btn = driver.find_elements(by=By.CSS_SELECTOR,value=".token-symbol-container")


# selecionando token primario
elemento_Btn[0].click()
driver.find_element(by=By.ID,value="token-search-input").send_keys(token0)
elemento = driver.find_element(by=By.CSS_SELECTOR,value=".css-1j6a53a ")

if elemento.text == token0:
    elemento.click()

# selecionando token secundario
elemento_Btn[1].click()
driver.find_element(by=By.ID,value="token-search-input").send_keys(token1)
elemento = driver.find_element(by=By.CSS_SELECTOR,value=".css-1j6a53a ")

if elemento.text == token1:
    elemento.click()

# inserindo a quantidade de token0

driver.find_element(by=By.CSS_SELECTOR,value=".token-amount-input").send_keys(qntd_token0)


elementos = driver.find_elements(by=By.CSS_SELECTOR,value=".rate-input-0")

for i in range(len(elementos)):
    if i == 1:
        driver.execute_script(f"document.querySelectorAll('.rate-input-0')[0].value={preco_Min}")
    else:
        driver.execute_script(f"document.querySelectorAll('.rate-input-0')[1].value={preco_max}")


driver.find_element(by=By.CSS_SELECTOR,value=".sc-dphd4z-11").click()
