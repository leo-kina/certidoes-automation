from selenium import webdriver
from config.settings import SETTINGS
from sites.socios.PedroHenriqueCoury.acoes_criminais_pedrao import emitir_acoes_criminal
from sites.socios.PedroHenriqueCoury.certidao_consta_nada_consta_pedrao import emitir_consta_nada_consta
from sites.socios.PedroHenriqueCoury.certidao_judicial_civel_negativa_pedrao import emitir_c_civel_judicial
from sites.socios.PedroHenriqueCoury.certidao_judicial_criminal_negativa_pedrao import emitir_c_judicial_criminal
from sites.socios.PedroHenriqueCoury.certidao_negativa_cadastro_nacional_condenacao_civeis_pedrao import emitir_negativa_cadastro_nacional_condenacao_civeis
from sites.socios.PedroHenriqueCoury.certidao_negativa_debitos_divida_ativa_pedrao import emitir_c_negativa_debitos_divida_ativa
from sites.socios.PedroHenriqueCoury.distribuicao_civel_pedrao import emitir_execucao_criminal
from sites.socios.PedroHenriqueCoury.execucao_criminal_pedrao import emitir_execucao_criminal
from sites.socios.PedroHenriqueCoury.falencia_concordatas_recuperacao_pedrao import emitir_falencia_concordatas_recuperacao


#python -m sites.socios.main

def main():
    driver = webdriver.Chrome()

    try:
        
        emitir_acoes_criminal(driver, url=SETTINGS["c_execucao_acoes_criminal"])

        emitir_consta_nada_consta(driver, url=SETTINGS["c_consta_nada_consta"])

        emitir_c_civel_judicial(driver, url=SETTINGS["c_judicial_civel_negativa_jf"])
    
        emitir_negativa_cadastro_nacional_condenacao_civeis(driver, url=SETTINGS["c_negativa_cadastro_nacional_condenacao_civeis"])

        emitir_c_judicial_criminal(driver, url=SETTINGS["c_judicial_criminal_negativa_jf"])

        emitir_c_negativa_debitos_divida_ativa(driver, url=SETTINGS["c_negativa_debitos_divida_ativa"])

        emitir_execucao_criminal(driver, url=SETTINGS["c_execucao_criminal"])

        emitir_execucao_criminal(driver, url=SETTINGS["c_distribuicao_civel"])

        emitir_falencia_concordatas_recuperacao(driver, url=SETTINGS["c_falencia_concordatas_recuperacao"])



    finally:
        print("Finalizado!")
        driver.quit()


if __name__ == "__main__":
    main()
