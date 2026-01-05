import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
email = "leonardo.kina@qitech.com.br"

def emitir_acoes_criminal(driver, dados):
    driver.get(dados["url"])
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))
    select_tipo = wait.until(
    EC.presence_of_element_located((By.ID, "cdModelo"))
    )

    Select(select_tipo).select_by_value("6")
    time.sleep(1.2)
    driver.find_element(By.ID, "tpPessoaJ").click()
    campo_nome = wait.until(
        EC.presence_of_element_located((By.ID, "nmCadastroJ"))
    )

    campo_nome.click()
    time.sleep(0.5)

    for char in dados["razao_social"]:
        campo_nome.send_keys(char)
        time.sleep(0.04)
    campo_cnpj = wait.until(
        EC.presence_of_element_located((By.ID, "identity.nuCnpjFormatado"))
    )

    campo_cnpj.click()
    time.sleep(0.5)

    for char in dados["cnpj"]:
        campo_cnpj.send_keys(char)
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
    print('Clique Enter para finalizar')
    input()


