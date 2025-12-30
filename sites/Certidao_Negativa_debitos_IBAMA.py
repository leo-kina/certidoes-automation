import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_c_negativa_debitos_ibama(driver, dados):
    endereco = "Avenida Rebouças, 2942, nos andares 7º ao 12º, em Pinheiros, São Paulo - SP"
    bairro = "Jardim Paulistano, São Paulo – SP"
    driver.get(dados["url"])
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    time.sleep(2)
    botao_selecionar = wait.until(
        EC.presence_of_element_located((By.ID, "lnk1"))
    )
    botao_selecionar.click()
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "p_num_cpf_cnpj"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.12)

    
    print("Digite manualmente o CAPTCHA, e depois clique no enter (no terminal)")
    input()
    botao_pesquisar = wait.until(
    EC.element_to_be_clickable((By.ID, "btnPesquisar"))
    )
    botao_pesquisar.click()
    time.sleep(2)

    nome_selecionar = wait.until(
        EC.presence_of_element_located((By.ID, "cad_nom_pessoa"))
    )
    nome_selecionar.click()
    for char in dados["razao_social"]:
        nome_selecionar.send_keys(char)
        time.sleep(0.12)
    input()
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
