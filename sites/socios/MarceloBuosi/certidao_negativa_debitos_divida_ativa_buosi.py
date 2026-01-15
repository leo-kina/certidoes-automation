import os
import glob
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from config.settings import SETTINGS


# python -m sites.socios.MarceloBuosi.certidao_negativa_debitos_divida_ativa_buosi

load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Marcelo Buosi"]
nome = socio["nome"]
cpf = socio["cpf"]


def emitir_c_negativa_debitos_divida_ativa(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    os.makedirs(pasta_final, exist_ok=True)

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))


    close_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//img[@onclick=\"Richfaces.hideModalPanel('modalPanelDebIpvaID')\"]")
))


    close_button.click()
    emitir_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[@href='/sc/pages/crda/emitirCrda.jsf']")
))


    emitir_button.click()

   
    campo_cpf = wait.until(
        EC.presence_of_element_located((By.ID, "emitirCrda:crdaInputCpf"))
    )
    campo_cpf.click()
    for char in cpf:
        campo_cpf.send_keys(char)
        time.sleep(0.12)

    time.sleep(0.2)
    print("Resolva o CAPTCHA e depois clique no ENTER")
    input()
    emitir_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@type='submit' and @value='Emitir']")
))


    emitir_btn.click()

    arquivo_pdf_novo = None
    timeout = time.time() + 20

    while time.time() < timeout:
        arquivos_depois = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
        novos = list(set(arquivos_depois) - set(arquivos_antes))
        if novos:
            arquivo_pdf_novo = novos[0]
            break
        time.sleep(0.4)

    if not arquivo_pdf_novo:
        print("Nenhum PDF foi baixado")
        return

    nome_final = (
        f"Certidão Negativa de Débitos Inscritos da Dívida Ativa "
        f"{nome}.pdf"
    )

    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)


if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_c_negativa_debitos_divida_ativa(
        driver=driver,
        url=SETTINGS["c_negativa_debitos_divida_ativa"]
    )

    print("Finalizado")
    driver.quit()
