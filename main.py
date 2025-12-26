from core.driver import criar_driver
from config.settings import SETTINGS
from data.data import empresas

from sites.certida_negativa_debitos_trabalhistas import emitir_cndt
from sites.certidao_regularidade_fgts import emitir_regularidade_fgts
from sites.Certidões_Distribuidores_Justiça_Trabalho1 import emitir_distribuidores_justica_trabalho1
from sites.Certidões_Distribuidores_Justiça_Trabalho2 import emitir_distribuidores_justica_trabalho2
from sites.Justica_Federal_da_3_Regiao_civiel import emitir_justica_3_civel 
from sites.Justica_Federal_da_3_Regiao_criminal import emitir_justica_3_criminal


def executar(site, empresa_key="SINGULARE"):
    dados = empresas.get(empresa_key)

    if not dados:
        print(f"Empresa '{empresa_key}' não encontrada")
        return

    url = SETTINGS.get(site)
    if not url:
        print(f"Site '{site}' não encontrado no SETTINGS")
        return

    dados["url"] = url
    driver = criar_driver()

    try:
        if site == "cndt":
            emitir_cndt(driver, dados)

        elif site == "regularidade_fgts":
            emitir_regularidade_fgts(driver, dados)

        elif site == "c_distribuidores_justica_trabalho1":
            emitir_distribuidores_justica_trabalho1(driver, dados)

        elif site == "c_distribuidores_justica_trabalho2":
            emitir_distribuidores_justica_trabalho2(driver, dados)
        elif site == "c_tribunal_regional_3_civel":
            emitir_justica_3_civel(driver, dados) 
        elif site == "c_tribunal_regional_3_criminal":
            emitir_justica_3_criminal(driver,dados)


        print(" Certidão emitida com sucesso")

    except Exception as e:
        print(f"Erro durante a emissão: {e}")

    finally:
        driver.quit()


def emitir_todas(empresa_key="SINGULARE"):
    executar("cndt", empresa_key)
    executar("regularidade_fgts", empresa_key)
    executar("c_distribuidores_justica_trabalho1", empresa_key)
    executar("c_distribuidores_justica_trabalho2", empresa_key)
    executar("c_tribunal_regional_3_civel", empresa_key)
    executar("c_tribunal_regional_3_criminal", empresa_key)


if __name__ == "__main__":
    executar("c_tribunal_regional_3_criminal", "SINGULARE")
    # emitir_todas("SINGULARE")
