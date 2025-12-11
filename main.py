from core.driver import criar_driver
from config.settings import SETTINGS
from sites.certida_negativa_debitos_trabalhistas import emitir_cndt
from sites.certidao_regularidade_fgts import emitir_regularidade_fgts
from data.data import empresas


def executar(site, empresa_key="SINGULARE"):


    dados = empresas.get(empresa_key)

    if not dados:
        print(f"Empresa '{empresa_key}' não encontrada no data.py")
        return


    dados["url"] = SETTINGS.get(site)

    if not dados["url"]:
        print(f"Site '{site}' não encontrado no SETTINGS.")
        return

    driver = criar_driver()

    try:
        if site == "cndt":
            emitir_cndt(driver, dados)

        elif site == "regularidade_fgts":
            emitir_regularidade_fgts(driver, dados)

        print("Certidão emitida com sucesso!")

    except Exception as e:
        print(f"Erro durante a emissão: {e}")

    finally:
        driver.quit()

def emitir_todas(empresa_key="SINGULARE"):
    executar("cndt", empresa_key)
    executar("regularidade_fgts", empresa_key)

if __name__ == "__main__":
    emitir_todas("SINGULARE")
