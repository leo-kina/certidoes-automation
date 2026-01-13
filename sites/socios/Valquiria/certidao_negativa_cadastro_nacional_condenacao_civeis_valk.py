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


# python -m sites.socios.Valquiria.certidao_negativa_cadastro_nacional_condenacao_civeis_valk

load_dotenv()

json_path = os.getenv("SOCIOS_JSON_PATH")

with open(json_path, "r", encoding="utf-8") as f:
    SOCIOS_JSON = json.load(f)

socio = SOCIOS_JSON["Valquiria Matsui"]
nome = socio["nome"]
cpf = socio["cpf"]


def emitir_negativa_cadastro_nacional_condenacao_civeis(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    os.makedirs(pasta_final, exist_ok=True)

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))


    wait.until(
        EC.element_to_be_clickable((By.ID, "tipoPessoaFisica"))
    ).click()

    time.sleep(1.2)

    campo_cpf = wait.until(
        EC.presence_of_element_located((By.ID, "num_cpf_cnpj"))
    )
    campo_cpf.click()
    time.sleep(0.5)

    for char in cpf:
        campo_cpf.send_keys(char)
        time.sleep(0.04)


    campo_nome = wait.until(
        EC.presence_of_element_located((By.ID, "nom_requerido"))
    )
    campo_nome.click()
    time.sleep(0.5)

    for char in nome:
        campo_nome.send_keys(char)
        time.sleep(0.04)

    print("Resolva o CAPTCHA e pressione Enter")
    input()

    wait.until(
        EC.element_to_be_clickable((By.ID, "btnPesquisarRequerido"))
    ).click()

    time.sleep(3)

    wait.until(
        EC.element_to_be_clickable((By.ID, "btnCertidaoNegativa"))
    ).click()

    print("Aguardando download do PDF...")

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
        f"Certidão Negativa Cadastro Nacional de Condenações Cíveis por Ato de Improbidade Administrativa e Inelegibilidade"
        f"{nome}.pdf"
    )

    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)


if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_negativa_cadastro_nacional_condenacao_civeis(
        driver=driver,
        url=SETTINGS["c_negativa_cadastro_nacional_condenacao_civeis"]
    )

    print("Finalizado")
    driver.quit()
