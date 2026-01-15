
from selenium import webdriver


#python test/site.py


def teste(driver, url):
    driver.get(url)
    driver.maximize_window()



    input()
if __name__ == "__main__":
    driver = webdriver.Chrome()

    teste(
        driver=driver,
        url="https://processo.stj.jus.br/processo/certidao/emissao"  
    )
    print("Finalizado")
    driver.quit()
