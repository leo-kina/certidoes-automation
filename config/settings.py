import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DOWNLOAD_DIR = os.path.join(BASE_DIR, "output", "certidoes_geradas")


SETTINGS = {
    "receita_federal": "https://exemplo.gov.br/certidao1",
    "justica_federal": "https://exemplo.jf.br/certidao2",
    "cndt": "https://cndt-certidao.tst.jus.br/inicio.faces",
}