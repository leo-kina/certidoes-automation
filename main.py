from dotenv import load_dotenv
import os

# Carrega .env usando caminho absoluto
load_dotenv("C:/Users/leonardo.kina/Desktop/DUE_aut/.env")

# Teste
CNPJ_SIN = os.getenv("CNPJ_SINGULARE")
print("DEBUG: CNPJ_SINGULARE =", CNPJ_SIN)
