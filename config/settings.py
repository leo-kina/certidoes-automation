import os
from dotenv import load_dotenv

load_dotenv()

SETTINGS = {
    "cndt": "https://cndt-certidao.tst.jus.br/inicio.faces",
    "regularidade_fgts": "https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf",
    "c_distribuidores_justica_trabalho2":"https://pje.trt2.jus.br/certidoes/trabalhista/emissao",
    "c_distribuidores_justica_trabalho1":"https://pje.trt1.jus.br/certidoes/trabalhista/emissao",
    "c_tribunal_regional_3_civel" : "https://web.trf3.jus.br/certidao-regional/",
    "c_tribunal_regional_3_criminal" : "https://web.trf3.jus.br/certidao-regional/",
    "c_conjunta_debitos_tributos_mobiliarios" :"https://duc.prefeitura.sp.gov.br/certidoes/forms_anonimo/frmConsultaEmissaoCertificado.aspx",
    "c_negativa_debitos_ibama":"https://servicos.ibama.gov.br/sicafiext/sistema.php",
    "c_ibama_embargo_regularidade":"https://servicos.ibama.gov.br/ctf/publico/areasembargadas/ConsultaPublicaAreasEmbargadas.php",
    "c_execucao_acoes_criminal": "https://esaj.tjsp.jus.br/sco/abrirCadastro.do",
    "c_execucao_criminal": "https://esaj.tjsp.jus.br/sco/abrirCadastro.do",
    "c_distribuicao_civel":"https://esaj.tjsp.jus.br/sco/abrirCadastro.do",
    "c_falencia_concordatas_recuperacao" : "https://esaj.tjsp.jus.br/sco/abrirCadastro.do",
    "c_feitos_gerais":"http://www.prt2.mpt.mp.br/index.php?option=com_mpt&view=certidaoneg",
    "c_negativa_cadastro_nacional_condenacao_civeis": "https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php",
    "c_acoes_trabalhista_tramitacao_processos_fisicos": "https://aplicacoes10.trt2.jus.br/certidao_trabalhista_eletronica/public/index.php/index/solicitacao",
    "c_negativa_correcional":"https://certidoes.cgu.gov.br/"

            
    }