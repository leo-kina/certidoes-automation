import os
from dotenv import load_dotenv

load_dotenv()

SETTINGS = {
    "cndt": "https://cndt-certidao.tst.jus.br/inicio.faces",
    "regularidade_fgts": "https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf"
}

CNPJS = {
    "QI_SDC": os.getenv("CNPJ_QI_SDC"),
    "QI_GESTORA": os.getenv("CNPJ_QI_GESTORA"),
    "QI_DISTRIBUIDORA": os.getenv("CNPJ_QI_DISTRIBUIDORA"),
    "SINGULARE": os.getenv("CNPJ_SINGULARE"),
}
