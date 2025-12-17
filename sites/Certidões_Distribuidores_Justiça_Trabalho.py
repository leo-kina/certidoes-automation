import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_distribuidores_justica_trabalho(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))


    
    time.sleep(1)

        
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "mat-input-0"))
    )
    campo_cnpj.click()
    time.sleep(1.2)
    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.16)
    print('Resolva o Captcha dps clique no Enter')
    input()
    botao_emitir = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[span[text()=" Emitir "]]'))
    )
    botao_emitir.click()
    time.sleep(7)
    botao_imprimir = driver.find_element(By.XPATH, '//button[span[text()="Imprimir"]]')
    botao_imprimir.click()
    time.sleep(1.4)
    botao_imprimir = driver.find_element(By.XPATH, '//button[span[text()="Imprimir"]]')
    botao_imprimir.click()




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

  
    nome_final = f"Certidao_Distribuidores_Justiça_Trabalho{dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)

 