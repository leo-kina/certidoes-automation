import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
email = "leonardo.kina@qitech.com.br"

def emitir_negativa_cadastro_nacional_condenacao_civeis(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()
    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

 
    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "num_cpf_cnpj"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
        time.sleep(0.04)
    
    campo_nome = wait.until(
        EC.presence_of_element_located((By.ID, "nom_requerido"))
    )

    campo_nome.click()
    time.sleep(0.5)

    for char in dados["razao_social"]:
        campo_nome.send_keys(char)
        time.sleep(0.04)
    print('Resolva Captcha e depois clique no Enter')
    input()
    botao_enviar = wait.until(
    EC.element_to_be_clickable((By.ID, "btnPesquisarRequerido"))
)

    botao_enviar.click()
    time.sleep(3)
    botao_emitir = wait.until(
    EC.element_to_be_clickable((By.ID, "btnCertidaoNegativa"))
)

    botao_emitir.click()
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

  
    nome_final = f"Certidão Negativa Cadastro Nacional de Condenações Cíveis por Ato de Improbidade Administrativa e Inelegibilidade {dados['nome']}.pdf"
    caminho_final = os.path.join(pasta_final, nome_final)

    os.rename(arquivo_pdf_novo, caminho_final)

    print("PDF salvo em:", caminho_final)


