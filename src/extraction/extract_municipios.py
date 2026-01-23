import requests
import json
from pathlib import Path

# URL da API do IBGE referente ao municípios
print("Iniciando extração de municípios")

URL_TEMPLATE = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF_ID}/municipios"

# caminho para salvar os dados crus
BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

STATES_FILE = RAW_DIR / "states.json"
OUTPUT_FILE = RAW_DIR / "municipios.json"

with open(STATES_FILE, "r", encoding="utf-8") as file:
    estados = json.load(file)

print(type(estados))
print(len(estados))
print(f"Estados carregados: {len(estados)}")

municipios = []

for estado in estados:
    id_estado = estado["id"]
    nome_estado = estado["nome"]

    print(f"Buscando municípios de {nome_estado}")

    url = URL_TEMPLATE.format(UF_ID=id_estado)
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        print(f"Municípios retornados: {len(dados)}")
        municipios.extend(dados)
    else:
        print(f"Erro ao buscar municípios de {nome_estado}")
        continue

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(municipios, file, ensure_ascii=False, indent=4)

print(f"Total de municípios coletados: {len(municipios)}")




