import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
email = "leonardo.kina@qitech.com.br"

def emitir_feitos_gerais(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    time.sleep(1.2)

    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "cnpj"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.04)
    print("Reolva o CAPTCHA, e depois clique no ENTER")
    input()
    botao_enviar = wait.until(
    EC.element_to_be_clickable((By.ID, "codin_consultar"))
)

    botao_enviar.click()
    print('Salve manualmene e depois clique no Enter')
    input()



