import csv
import psycopg2
from pathlib import Path

# caminho do CSV tratado
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "municipios.csv"

# configurações do banco
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="etl_ibge_db",
    user="postgres",
    password="dany"
)

cur = conn.cursor()

print("Conectado ao banco com sucesso!")

# ler CSV e inserir os dados
with open(CSV_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO municipios (municipio_id, municipio_nome, estado_id, estado_sigla, estado_nome)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            int(row["municipio_id"]),
            row["municipio_nome"],
            int(row["estado_id"]),
            row["estado_sigla"],
            row["estado_nome"]

        ))

conn.commit()
print("Dados carregados no PostgreSQL com sucesso!")

cur.close()
conn.close()