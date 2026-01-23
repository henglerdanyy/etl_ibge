import json
import csv
from pathlib import Path

print("Iniciando transformação dos dados de municípios.")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

MUNICIPIOS_FILE = RAW_DIR / "municipios.json"
STATES_FILE = RAW_DIR / "states.json"
OUTPUT_FILE = PROCESSED_DIR / "municipios.csv"

print("Lendo municípios de:", MUNICIPIOS_FILE)
print("Lendo estados de:", STATES_FILE)
print("Salvando CSV em:", OUTPUT_FILE)

# leitura dos dados brutos
with open(MUNICIPIOS_FILE, "r", encoding="utf-8") as f:
    municipios = json.load(f)

with open(STATES_FILE, "r", encoding="utf-8") as f:
    estados = json.load(f)

print("Tipo municípios:", type(municipios))
print("Quantidade municipios:", len(municipios))

print("Tipo estados:", type(estados))
print("Quantidade estados:", len(estados))

dados_tratados = []
registros_ignorados = 0

for municipio in municipios:
    microrregiao = municipio.get("microrregiao")

    if microrregiao is None:
        registros_ignorados += 1
        continue

    mesorregiao = microrregiao.get("mesorregiao")
    if mesorregiao is None:
        registros_ignorados += 1
        continue

    uf = mesorregiao.get("UF")
    if uf is None:
        registros_ignorados += 1
        continue

    registro = {
        "municipio_id": municipio["id"],
        "municipio_nome": municipio["nome"],
        "estado_id": uf["id"],
        "estado_sigla": uf["sigla"],
        "estado_nome": uf["nome"],
    }

    dados_tratados.append(registro)

print("Total de registros tratados:", len(dados_tratados))
print("Total de registros ignorados:", registros_ignorados)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "municipio_id",
        "municipio_nome",
        "estado_id",
        "estado_sigla",
        "estado_nome",
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dados_tratados)

print("Arquivo CSV de municípios criado com sucesso!")