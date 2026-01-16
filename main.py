from core.driver import criar_driver
from config.settings import SETTINGS
from data.data import empresas

from sites.certida_negativa_debitos_trabalhistas import emitir_cndt
from sites.certidao_regularidade_fgts import emitir_regularidade_fgts
from sites.Certidões_Distribuidores_Justiça_Trabalho1 import emitir_distribuidores_justica_trabalho1
from sites.Certidões_Distribuidores_Justiça_Trabalho2 import emitir_distribuidores_justica_trabalho2
from sites.Justica_Federal_da_3_Regiao_civiel import emitir_justica_3_civel 
from sites.Justica_Federal_da_3_Regiao_criminal import emitir_justica_3_criminal
from sites.Certidao_conjunta_Debitos_Tributos_Mobiliarios import emitir_c_conjunta_mobiliarios
from sites.Certidao_Negativa_debitos_IBAMA import emitir_c_negativa_debitos_ibama
from sites.Certidao_regulridade_embargos_IBAMA import emitir_c_embargos_regularidades_ibama
from sites.Certidao_acoes_criminais import emitir_acoes_criminal
from sites.Certidao_execucao_criminal import emitir_execucao_criminal
from sites.certidao_distribuicao_civel import emitir_distribuicao_civel
from sites.certidao_falencia_concordatas_recuperacao import emitir_falencia_concordatas_recuperacao
from sites.ceritdao_feitos_gerais import emitir_feitos_gerais
from sites.certidao_negativa_cadastro_nacional_condenacao_civeis import emitir_negativa_cadastro_nacional_condenacao_civeis
from sites.certidao_acaoa_trabalhista_processos_fisicos import emitir_c_processos_acaoa_trabalhista_processos_fisicos
from sites.Certidao_Negativa_Correcional import emitir_c_negativa_correcional
from sites.certidao_judicial_criminal_negativa_jf import emitir_c_judicial_criminal
from sites.certidao_judicial_civel_negativa_jf import emitir_c_civel_judicial_criminal
from sites.certidao_negativa_debitos_divida_ativa import emitir_c_negativa_debitos_divida_ativa
from sites.certidao_consta_nada_consta import emitir_consta_nada_consta
def executar(site, empresa_key):
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
        print(f"\n📄 Emitindo certidão: {site}")
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
        elif site == "c_conjunta_debitos_tributos_mobiliarios":
            emitir_c_conjunta_mobiliarios(driver,dados)
        elif site == "c_negativa_debitos_ibama":
            emitir_c_negativa_debitos_ibama(driver,dados)
        elif site == "c_ibama_embargo_regularidade":
            emitir_c_embargos_regularidades_ibama(driver, dados)
        elif site == "c_execucao_acoes_criminal":
            emitir_acoes_criminal(driver,dados)
        elif site == "c_execucao_criminal":
            emitir_execucao_criminal(driver,dados)
        elif site == "c_distribuicao_civel":
            emitir_distribuicao_civel(driver,dados)
        elif site == "c_falencia_concordatas_recuperacao":
            emitir_falencia_concordatas_recuperacao(driver,dados)
        elif site == "c_feitos_gerais":
            emitir_feitos_gerais(driver,dados)
        elif site == "c_negativa_cadastro_nacional_condenacao_civeis":
            emitir_negativa_cadastro_nacional_condenacao_civeis(driver,dados)
        elif site == "c_acoes_trabalhista_tramitacao_processos_fisicos":
            emitir_c_processos_acaoa_trabalhista_processos_fisicos(driver,dados)
        elif site == "c_negativa_correcional":
            emitir_c_negativa_correcional(driver,dados)
        elif site == "c_judicial_criminal_negativa_jf":
            emitir_c_judicial_criminal(driver,dados)
        elif site == "c_judicial_civel_negativa_jf":
            emitir_c_civel_judicial_criminal(driver,dados)
        elif site == "c_negativa_debitos_divida_ativa":
            emitir_c_negativa_debitos_divida_ativa(driver,dados)
        elif site == "c_consta_nada_consta":
            emitir_consta_nada_consta(driver,dados)



        
        


        print("Certidão emitida com sucesso")

    except Exception as e:
        print(f"Erro durante a emissão: {e}")

    finally:
        driver.quit()


def emitir_todas(empresa_key):
    executar("cndt", empresa_key)
    executar("regularidade_fgts", empresa_key)
    executar("c_distribuidores_justica_trabalho1", empresa_key)
    executar("c_distribuidores_justica_trabalho2", empresa_key)
    executar("c_tribunal_regional_3_civel", empresa_key)
    executar("c_tribunal_regional_3_criminal", empresa_key)
    executar("c_conjunta_debitos_tributos_mobiliarios", empresa_key) 
    executar("c_negativa_debitos_ibama", empresa_key) 
    executar("c_ibama_embargo_regularidade", empresa_key)
    executar("c_execucao_acoes_criminal", empresa_key)
    executar("c_execucao_criminal", empresa_key)
    executar("c_distribuicao_civel", empresa_key)
    executar("c_falencia_concordatas_recuperacao", empresa_key)
    executar("c_feitos_gerais", empresa_key)
    executar("c_negativa_cadastro_nacional_condenacao_civeis", empresa_key)
    executar("c_acoes_trabalhista_tramitacao_processos_fisicos", empresa_key)
    executar("c_negativa_correcional", empresa_key)
    executar("c_judicial_criminal_negativa_jf", empresa_key)
    executar("c_judicial_civel_negativa_jf", empresa_key)
    executar("c_negativa_debitos_divida_ativa", empresa_key)
    executar("c_consta_nada_consta", empresa_key)


if __name__ == "__main__":
    #executar("c_ibama_embargo_regularidade", "SINGULARE")
    #executar("c_negativa_correcional", "SINGULARE")
    #executar("c_judicial_criminal_negativa_jf", "QI_GESTORA")

    
    #certidoes de acao e execucao crimianl, sempre precisa ter um intervalo de 1 dia para funcionar 

   #executar("c_consta_nada_consta", "QI_GESTORA")
    
    executar("c_negativa_debitos_divida_ativa", "SINGULARE")

    emitir_todas("QI_GESTORA")
