from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import DOWNLOAD_DIR

def criar_driver():
    options = webdriver.ChromeOptions()

    # 👇 aponta para o Chrome instalado
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    options.add_argument("--start-maximized")
    options.add_experimental_option(
        "prefs",
        {
            "download.prompt_for_download": False,
            "download.default_directory": DOWNLOAD_DIR,
            "plugins.always_open_pdf_externally": True,
        },
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver
