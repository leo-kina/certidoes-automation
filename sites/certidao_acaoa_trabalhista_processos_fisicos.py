import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def emitir_c_processos_acaoa_trabalhista_processos_fisicos(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    botao_radio = wait.until(
        EC.presence_of_element_located((By.ID, "tipoDocumentoPesquisado-2"))
    )
    botao_radio.click()

   
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "numeroDocumentoPesquisado"))
    )
    campo_cnpj.click()
    time.sleep(0.5)

 
    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)

    campo_razao = wait.until(
    EC.presence_of_element_located((By.ID, "nomePesquisado"))
    )
    campo_razao.click()
    time.sleep(0.5)

 
    for char in dados["razao_social"]:
        campo_razao.send_keys(char)
        time.sleep(0.12)
    

    print('Resolva o Captcha e depois clique no enter')
    input()

    botao_emitir = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
    botao_emitir.click()
    botao = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@onclick, 'recuperarcertidao')]")
    )
    )
    botao.click()
    print("Aguardando download do PDF")
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

  
    nome_final = f"Certidao_ação_trabalhista_processos_fisicos{dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)
