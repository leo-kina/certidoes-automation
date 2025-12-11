import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def emitir_cndt(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    botao_emitir_inicial = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Emitir Certidão']"))
    )
    botao_emitir_inicial.click()

   
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "gerarCertidaoForm:cpfCnpj"))
    )
    campo_cnpj.click()
    time.sleep(0.5)

 
    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)
    
    print("Digite manualmente o CAPTCHA, e depois clique no enter (no terminal)")
    input()
    botao_emitir_final = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Emitir Certidão']"))
    )
    botao_emitir_final.click()

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

  
    nome_final = f"Certidao_Negativa_Debitos_{dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)
