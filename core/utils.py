
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def esperar_elemento(driver, by, value, timeout=10):
    for _ in range(timeout):
        try:
            elemento = driver.find_element(by, value)
            return elemento
        except NoSuchElementException:
            time.sleep(1)
    raise Exception(f"Elemento não encontrado: {value}")


def preencher(driver, by, value, texto):
    campo = esperar_elemento(driver, by, value)
    campo.clear()
    campo.send_keys(texto)

