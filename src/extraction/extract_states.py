import requests
import json
from pathlib import Path

# URL da API do IBGE
URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

# caminho para salvar os dados crus
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DIR / "states.json"

print("BASE_DIR", BASE_DIR)
print("RAW_DIR:", RAW_DIR)
print("OUTPUT_FILE:", OUTPUT_FILE)

response = requests.get(URL)

print("Status code:", response.status_code)

data = response.json()
print("Tipo do dado:", type(data))
print("Quantidade de registros:", len(data))

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

    print("Arquivo JSON salvo com sucesso!")


