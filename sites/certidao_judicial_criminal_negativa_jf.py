import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.data import email

def emitir_c_judicial_criminal(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    driver.execute_script("""
    const radio = document.getElementById('cnpj');
    radio.checked = true;
    radio.dispatchEvent(new Event('change', { bubbles: true }));
""")

   
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.XPATH,
    "//input[@name='cpfCnpj']"
        ))
    )
    campo_cnpj.click()
    time.sleep(0.5)

 
    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.05)

    campo_email = wait.until(
    EC.presence_of_element_located((By.ID, "email"))
)

    campo_email.click()
    time.sleep(0.5)

 
    for char in email:
        campo_email.send_keys(char)
        time.sleep(0.04)
    campo_confirmar = wait.until(
    EC.presence_of_element_located((By.ID, "emailConfirmacao"))
)

    campo_confirmar.click()
    time.sleep(0.5)

 
    for char in email:
        campo_confirmar.send_keys(char)
        time.sleep(0.04)
    botao = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[text()='Solicitar certidão']]"
    ))
)
    driver.execute_script("arguments[0].click();", botao)

    print("Certidao emitida! fique de olho em seu email")

