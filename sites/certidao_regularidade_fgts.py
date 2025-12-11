import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def emitir_regularidade_fgts(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)


    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "mainForm:txtInscricao1"))
    )
    campo_cnpj.click()
    time.sleep(0.5)


    cnpj = dados["cnpj"]
    print("Digitando CNPJ manualmente...")
    for char in cnpj:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)


    input("Confira o CNPJ na tela e pressione ENTER para continuar...")


    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Consultar']"))
    )
    botao_emitir.click()

    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.ID, "mainForm:j_id51"))
    )

    input("Pressione ENTER para finalizar...")

