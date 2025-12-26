import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_justica_3_criminal(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))


    
    time.sleep(1)

    botao_solicitar = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'btn-primary') and contains(text(),'Solicitar')]"))
    )
    botao_solicitar.click()
    time.sleep(1.2)
    
    select_tipo = wait.until(
    EC.presence_of_element_located((By.ID, "Tipo"))
    )

    Select(select_tipo).select_by_value("CRIMINAL")
    time.sleep(1.2)

    select_doc = wait.until(
    EC.presence_of_element_located((By.ID, "TipoDeDocumento"))
    )


    Select(select_doc).select_by_value("CNPJ")
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "Documento"))
    )
    campo_cnpj.click()
    time.sleep(1.2)
    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.16)

    select_abrangencia = wait.until(
    EC.presence_of_element_located((By.ID, "TipoDeAbrangencia"))
    )

    Select(select_abrangencia).select_by_value("TRF")
    print('Resolva o Captcha dps clique no Enter')
    input()
    botao_emitir = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
    )

    botao_emitir.click()
    print('Salve manualmente, quando terminar clique no enter')
    input()




   
 