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


#python -m sites.socios.Valquiria.execucao_criminal_valk




load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Valquiria Matsui"]
nome = socio["nome"]
cpf = socio["cpf"]
rg = socio['rg']
nome_mae= socio["mae"]
nome_pai= socio["pai"]
nascimento = socio["nascimento"]
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
        time.sleep(0.04)
    campo_cpf = wait.until(
        EC.presence_of_element_located((By.ID, "identity.nuCpfFormatado"))
    )

    campo_cpf.click()
    time.sleep(0.5)

    for char in cpf:
        campo_cpf.send_keys(char)
        time.sleep(0.04)
    
    campo_rg = wait.until(
        EC.presence_of_element_located((By.ID, "identity.nuRgFormatado"))
    )

    campo_rg.click()
    time.sleep(0.5)

    for char in rg:
        campo_rg.send_keys(char)
        time.sleep(0.04)
    campo_genero_m = wait.until(
    EC.element_to_be_clickable((By.ID, "flGeneroM"))
    )
    campo_genero_m.click()

    campo_mae = wait.until(
        EC.presence_of_element_located((By.ID, "nmMaeCadastro"))
    )

    campo_mae.click()
    time.sleep(0.5)

    for char in nome_mae:
        campo_mae.send_keys(char)
        time.sleep(0.04)
    campo_pai = wait.until(
        EC.presence_of_element_located((By.ID, "nmPaiCadastro"))
    )

    campo_pai.click()
    time.sleep(0.5)

    for char in nome_pai:
        campo_pai.send_keys(char)
        time.sleep(0.04)
    campo_nacimento = wait.until(
        EC.presence_of_element_located((By.ID, "dataNascimento"))
    )

    campo_nacimento.click()
    time.sleep(0.5)

    for char in nascimento:
        campo_nacimento.send_keys(char)
        time.sleep(0.04)
    campo_email = wait.until(
        EC.presence_of_element_located((By.ID, "identity.solicitante.deEmail"))
    )

    campo_email.click()
    time.sleep(0.5)

    for char in email:
        campo_email.send_keys(char)
        time.sleep(0.04)
    checkbox = wait.until(
    EC.element_to_be_clickable((By.ID, "confirmacaoInformacoes"))
)
    checkbox.click()
    botao_enviar = wait.until(
    EC.element_to_be_clickable((By.ID, "pbEnviar"))
)

    botao_enviar.click()




if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_execucao_criminal(
        driver=driver,
        url=SETTINGS["c_execucao_acoes_criminal"]  
    )
    print("Finalizado")
    driver.quit()
