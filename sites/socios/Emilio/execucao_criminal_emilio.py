import os
import glob
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
from data.data import email
from config.settings import SETTINGS
#python -m sites.socios.Emilio.execucao_criminal_emilio


load_dotenv()

def emitir_execucao_criminal(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    pasta_downloads = r"C:\Users\leonardo.kina\Downloads"
    pasta_final = r"C:\Users\leonardo.kina\Downloads\Certidoes_teste"

    arquivos_antes = glob.glob(os.path.join(pasta_downloads, "*.pdf"))

    print("Teste")
    input("")

if __name__ == "__main__":
    driver = webdriver.Chrome()

    emitir_execucao_criminal(
        driver=driver,
        url=SETTINGS["c_execucao_criminal"]  
    )
    print("Finalizado")
    driver.quit()
