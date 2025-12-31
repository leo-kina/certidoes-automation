import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_c_embargos_regularidades_ibama(driver, dados):

    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    time.sleep(2)
    botao_entrar = driver.find_element(By.ID, "btnEntrar")
    botao_entrar.click()
    time.sleep(2)
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "num_cpf_cnpj"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.06)

    botao_selecionar = wait.until(
        EC.presence_of_element_located((By.ID, "Emitir_Certificado"))
    )
    botao_selecionar.click()

    
    print("Salve Manualmente")
    input()
   
