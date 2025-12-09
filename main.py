from core.driver import criar_driver
from config.settings import SETTINGS
from sites.certida_negativa_debitos_trabalhistas import emitir_cndt


def executar(site, cnpj=None):
    driver = criar_driver()

    dados = {
        "cnpj": cnpj,
        "url": SETTINGS.get(site),
    }

    try:
        if site == "cndt":
            emitir_cndt(driver, dados)
        else:
            print("Site não configurado.")
            return

        print("✔️ Certidão emitida!")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    executar("cndt", cnpj="62285390000140")
