
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


#python test/site.py


def teste(driver, url):
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    input()
if __name__ == "__main__":
    driver = webdriver.Chrome()

    teste(
        driver=driver,
        url="https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php"  
    )
    print("Finalizado")
    driver.quit()
