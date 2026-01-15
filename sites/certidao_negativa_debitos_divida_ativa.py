import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def emitir_c_negativa_debitos_divida_ativa(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    close_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//img[@onclick=\"Richfaces.hideModalPanel('modalPanelDebIpvaID')\"]")
))


    close_button.click()
    emitir_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[@href='/sc/pages/crda/emitirCrda.jsf']")
))


    emitir_button.click()

   
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "emitirCrda:crdaInputCnpjBase"))
    )
    campo_cnpj.click()
    for char in dados["cnpj_base"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)

    time.sleep(0.2)
    print("Resolva o CAPTCHA e depois clique no ENTER")
    input()
    emitir_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@type='submit' and @value='Emitir']")
))


    emitir_btn.click()

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

  
    nome_final = f"Certidao_negativa_debitos_inscritos_divida_ativa{dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)
