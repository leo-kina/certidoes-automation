import os
import glob
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from data.data import email
from config.settings import SETTINGS
from selenium.webdriver.support.ui import Select
import json
from dotenv import load_dotenv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#python -m sites.socios.ThiagoIsilian.certidao_judicial_criminal_negativa_thiago




load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Thiago Bott"]
cpf = socio["cpf"]
def emitir_c_judicial_criminal(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)
    driver.execute_script("""
    const radio = document.getElementById('cpf');
    radio.checked = true;
    radio.dispatchEvent(new Event('change', { bubbles: true }));
""")

   
    campo_cpf = wait.until(
        EC.presence_of_element_located((By.XPATH,
    "//input[@name='cpfCnpj']"
        ))
    )
    campo_cpf.click()
    time.sleep(0.5)

 
    for char in cpf:
        campo_cpf.send_keys(char)
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
    print("Espere a confirmacao e depois clique no Enter")
    input()

   




if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_c_judicial_criminal(
        driver=driver,
        url=SETTINGS["c_judicial_criminal_negativa_jf"]  
    )
    print("Finalizado")
    driver.quit()
