import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_consta_nada_consta(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)


    select_element = wait.until(EC.presence_of_element_located((By.ID, "idCertidaoTipoCombo")))


    select = Select(select_element)


    select.select_by_value("pessoajuridicaconstanadaconsta")
    time.sleep(1.2)
    
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "idParteCNPJ"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)
    botao_emitir = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@type='button' and @value=' Emitir Certidão ']")
))


    botao_emitir.click()
    
    print("Salve Manualmente e depois clique no ENTER")
    input()



  
