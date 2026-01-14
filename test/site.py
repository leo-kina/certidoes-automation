
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
        url="https://aplicacoes10.trt2.jus.br/certidao_trabalhista_eletronica/public/index.php/index/solicitacao"  
    )
    print("Finalizado")
    driver.quit()
