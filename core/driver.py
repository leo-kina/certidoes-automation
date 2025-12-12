from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def criar_driver():
    chrome_options = Options()

    # impede detecção do webdriver
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # melhora compatibilidade
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # não rodar headless (Cloudflare detecta)
    # chrome_options.add_argument("--headless=new")  # só use se necessário

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # remove flag de automação pelo JS
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver
