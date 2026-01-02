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


#python -m sites.socios.Emilio.execucao_criminal_emilio




load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Emilio Moreira"]
nome = socio["nome"]
1
def emitir_execucao_criminal(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    select_tipo = wait.until(
    EC.presence_of_element_located((By.ID, "cdModelo"))
    )

    Select(select_tipo).select_by_value("94")
    time.sleep(1.2)
    campo_nome = wait.until(
        EC.presence_of_element_located((By.ID, "nmCadastroF"))
    )

    campo_nome.click()
    time.sleep(0.5)

    for char in nome:
        campo_nome.send_keys(char)
        time.sleep(0.12)

    
    print("Teste")
    input("")

if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_execucao_criminal(
        driver=driver,
        url=SETTINGS["c_execucao_criminal"]  
    )
    print("Finalizado")
    driver.quit()
