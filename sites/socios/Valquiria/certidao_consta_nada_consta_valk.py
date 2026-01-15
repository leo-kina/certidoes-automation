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


#python -m sites.socios.Valquiria.certidao_consta_nada_consta_valk




load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Valquiria Matsui"]
cpf = socio["cpf"]
def emitir_consta_nada_consta(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)
   
    select_element = wait.until(EC.presence_of_element_located((By.ID, "idCertidaoTipoCombo")))


    select = Select(select_element)


    select.select_by_value("pessoafisicaconstanadaconsta")
    time.sleep(1.2)
    
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "idParteCPF"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in cpf:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)
    botao_emitir = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@type='button' and @value=' Emitir Certidão ']")
))


    botao_emitir.click()
    
    print("Salve Manualmente e depois clique no ENTER")
    input()




   




if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_consta_nada_consta(
        driver=driver,
        url=SETTINGS["c_consta_nada_consta"]  
    )
    print("Finalizado")
    driver.quit()
