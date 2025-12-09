import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def emitir_cndt(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)


    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Emitir Certidão']"))
    )
    botao_emitir.click()


    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "gerarCertidaoForm:cpfCnpj"))
    )
    campo_cnpj.click()  
    time.sleep(0.5)     


    cnpj = dados["cnpj"]
    print("⌨️ Digitando CNPJ manualmente...")
    for char in cnpj:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)  

    print("⚠️ Resolva o CAPTCHA manualmente e depois pressione Enter no terminal.")
    input()


    botao_gerar = wait.until(
        EC.element_to_be_clickable((By.ID, "gerarCertidaoForm:botaoGerar"))
    )
    botao_gerar.click()
    print("📄 Certidão sendo gerada...")
