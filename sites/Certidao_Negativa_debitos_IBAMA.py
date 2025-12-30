import time
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def emitir_c_negativa_debitos_ibama(driver, dados):
    endereco = "Avenida Rebouças, 2942, 7º ao 12º, Pinheiros"
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
        time.sleep(0.07)
    endereco_selecionar = wait.until(
    EC.presence_of_element_located((By.ID, "cad_end_pessoa"))
    )
    endereco_selecionar.click()
    for char in endereco:
        endereco_selecionar.send_keys(char)
        time.sleep(0.06)
    bairro_selecionar = wait.until(
    EC.presence_of_element_located((By.ID, "cad_des_bairro"))
    )
    bairro_selecionar.click()
    for char in bairro:
        bairro_selecionar.send_keys(char)
        time.sleep(0.06)
    
    select_uf = Select(
    wait.until(EC.presence_of_element_located((By.ID, "cad_cod_uf")))
    )   

    select_uf.select_by_value("35")
    time.sleep(1)
    select_mun = Select(
        wait.until(EC.presence_of_element_located((By.ID, "cad_cod_municipio")))
        )   
    select_mun.select_by_value("3550308")
    time.sleep(0.4)
    botao_confirmar = wait.until(
    EC.element_to_be_clickable((By.ID, "btnConfirmar"))
)
    botao_confirmar.click()
    time.sleep(3)
    botao_confirmar = wait.until(EC.element_to_be_clickable((By.ID, "btnConfirmar")))
    print('Salve manualmente')
    input()
