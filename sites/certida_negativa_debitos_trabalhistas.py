import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def emitir_cndt(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # 1️⃣ Clicar no botão "Emitir Certidão"
    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Emitir Certidão']"))
    )
    botao_emitir.click()

    # 2️⃣ Esperar campo CNPJ aparecer
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "gerarCertidaoForm:cpfCnpj"))
    )
    campo_cnpj.click()  # garante que o campo está com foco
    time.sleep(0.5)     # pequena pausa para foco

    # 3️⃣ Digitar caractere por caractere
    cnpj = dados["cnpj"]
    print("⌨️ Digitando CNPJ manualmente...")
    for char in cnpj:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)  # pausa entre cada caractere para simular digitação

    # 4️⃣ Resolver CAPTCHA manualmente
    print("⚠️ Resolva o CAPTCHA manualmente e depois pressione Enter no terminal.")
    input()

    # 5️⃣ Clicar no botão "Gerar Certidão"
    botao_gerar = wait.until(
        EC.element_to_be_clickable((By.ID, "gerarCertidaoForm:botaoGerar"))
    )
    botao_gerar.click()
    print("📄 Certidão sendo gerada...")
