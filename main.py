from core.driver import criar_driver
from config.settings import SETTINGS
from sites.certida_negativa_debitos_trabalhistas import emitir_cndt
from sites.certidao_regularidade_fgts import emitir_regularidade_fgts
from sites.Certidao_Promotoria_Justica_Estadual import emitir_c_promotoria_justica_estadual
from data.data import empresas, razao_social
from sites.Certidões_Distribuidores_Justiça_Trabalho import emitir_distribuidores_justica_trabalho

def executar(site, empresa_key="SINGULARE", razao_key="RSINGULARE"):


    dados = empresas.get(empresa_key)
    razao_social1 = razao_social.get(razao_key)

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
        elif site == "c_promotoria_justica_estadual":
            emitir_c_promotoria_justica_estadual(driver,razao_social1,dados)
            print("Certidao emitida")
        elif site ==  "emitir_distribuidores_justica_trabalho":
            emitir_distribuidores_justica_trabalho(driver, dados)
            print("Certidao emitida")
     
        

    except Exception as e:
        print(f"Erro durante a emissão: {e}")

    finally:
        driver.quit()

def emitir_todas(empresa_key="SINGULARE"):
    executar("cndt", empresa_key)
    executar("regularidade_fgts", empresa_key)
    executar("cn_tributos_municipais",empresa_key)
    #executar("c_promotoria_justica_estadual",empresa_key, "RSINGULARE")
    executar("c_distribuidores_justica_trabalho", empresa_key)

if __name__ == "__main__":
    #executar("c_promotoria_justica_estadual", "SINGULARE", "RSINGULARE")
    executar("c_distribuidores_justica_trabalho", "SINGULARE")
    #emitir_todas("QI_GESTORA")
