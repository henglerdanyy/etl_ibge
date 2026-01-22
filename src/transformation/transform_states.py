import json
import pandas as pd
from pathlib import Path

# caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "states.json"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = PROCESSED_DIR / "states.csv"

def transform_states():
    with open(RAW_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # normaliza o JSON (a região vira colunas)
    df = pd.json_normalize(
        data,
        sep="_"
    )

    # seleciona e renomeia colunas
    df = df[[
        "id",
        "sigla",
        "nome",
        "regiao_id",
        "regiao_sigla",
        "regiao_nome"
    ]]

    df.rename(columns={
        "id": "state_id",
        "sigla": "state_code",
        "nome": "state_name",
        "regiao_id": "region_id",
        "regiao_sigla": "region_code",
        "regiao_nome": "region_name"
    }, inplace=True)

    # salva CSV tratado
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"Arquivo transofmrado salvo em: {OUTPUT_FILE}")
    print(f"Total de estados: {len(df)}")

if __name__ == "__main__":
    transform_states()

