import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import base64

def salvar_pdf(driver, caminho):
    print_options = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True
    }

    result = driver.execute_cdp_cmd("Page.printToPDF", print_options)

  
    data = base64.b64decode(result['data'])

    with open(caminho, "wb") as f:
        f.write(data)

    print("PDF salvo em:", caminho)

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

    select_estado = Select(driver.find_element(By.ID, "mainForm:uf"))
    select_estado.select_by_visible_text("SP")


    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Consultar']"))
    )
    botao_emitir.click()

    link = wait.until(
        EC.element_to_be_clickable((By.ID, "mainForm:j_id51"))
    )
    link.click()
    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Visualizar']"))
    )
    botao_emitir.click()
    salvar_pdf(driver, "crf_fgts.pdf")


    

