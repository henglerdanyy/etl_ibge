# ETL Pipeline com Dados do IBGE

## 📌 Descrição

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) em Python
utilizando dados públicos disponibilizados pela API do IBGE.
O objetivo é coletar, tratar e armazenar dados geográficos e populacionais
para análises posteriores.

Projeto desenvolvido como parte dos estudos em Ciência de Dados com Python,
com foco em boas práticas de organização e engenharia de dados.

## 🎯 Objetivo

- Aprender e praticar a construção de pipelines ETL em Python
- Consumir APIs públicas reais
- Separar corretamente as etapas de extração, transformação e carregamento
- Estruturar um projeto de dados de forma organizada e escalável

## 🧭 Escopo Inicial

O projeto será desenvolvido em etapas:

1. Extração dos dados de estados brasileiros
2. Extração dos dados de municípios por estado

## 📁 Estrutura do Projeto

 - etl_ibge
   - src
     - extraction
       - extract_states.py
       - extract_municipios.py
     - transformation
        - transform_states.py
        - transform_municipios.py
     - load
        - load_municipios.py
   - data
     - raw
       - states.json
       - municipios.json
    - processed
       - states.csv
       - municipios.csv
   - README.md


## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Requests
- JSON
- Pandas 
- PostgreSQL

## 🔄 Pipeline ETL

### Extração (Extract)
- Consumo da API pública do IBGE
- Coleta dos dados de estados brasileiros
- Armazenamento dos dados brutos em formato JSON (`data/raw/states.json`)

### Transformação (Transform)
- Leitura do JSON bruto
- Seleção e normalização dos campos relevantes
- Conversão dos dados para formato CSV
- Salvamento em `data/processed/states.csv`

### Carga (Load)
- Inserção dos dados tratados no PostgreSQL
- Tabela relacional para municípios.

## 🗄️ Banco de Dados

Banco utilizado: PostgreSQL

Tabela criada:
    - municipios

Campos:
- municipio_id
- municipio_nome
- estado_id
- estado_sigla
- estado_nome

## 🚧 Status do Projeto

Projeto concluído.

Pipeline ETL funcional com dados reais do IBGE, incluindo carga em banco de dados PostgreSQL.

Alvo de possíveis atualizações escaláveis futuras.



