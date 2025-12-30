import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_c_conjunta_mobiliarios(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    select_tipo = wait.until(
    EC.presence_of_element_located((By.ID, "ctl00_ConteudoPrincipal_ddlTipoCertidao"))
    )

    Select(select_tipo).select_by_value("1")
    time.sleep(1.2)
    
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "ctl00_ConteudoPrincipal_txtCNPJ"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)

    
    print("Digite manualmente o CAPTCHA, e depois clique no enter (no terminal)")
    input()
    driver.find_element(By.ID, "ctl00_ConteudoPrincipal_btnEmitir").click()

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

  
    nome_final = f"Certidao_Conjunta_Debitos_Tributos_Mobiliarios{dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)
