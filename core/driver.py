from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def criar_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")


    driver = webdriver.Chrome(options=options)
    return driver
