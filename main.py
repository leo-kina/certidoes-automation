from core.driver import criar_driver
from config.settings import SETTINGS, CNPJS
from sites.certida_negativa_debitos_trabalhistas import emitir_cndt
from sites.certidao_regularidade_fgts import emitir_regularidade_fgts

def executar(site, cnpj_key="SINGULARE"):
    driver = criar_driver()
    
    dados = {
        "cnpj": CNPJS.get(cnpj_key),
        "url": SETTINGS.get(site),
    }

    try:
        if site == "cndt":
            emitir_cndt(driver, dados)
        elif site == "regularidade_fgts":
            emitir_regularidade_fgts(driver, dados)
        else:
            print("Site não configurado.")
            return

        print("Certidão emitida!")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    executar("regularidade_fgts")
    
