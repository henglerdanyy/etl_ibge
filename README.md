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
3. Extração de dados populacionais por município e ano

## 📁 Estrutura do Projeto

 - etl_ibge
   - src
     - extraction
       - extract_states.py
       - extract_municipios.py
     - transformation
        - transform_states.py
        - transform_municipios.py
   - data
     - raw
       - states.json
       - municipios.json
    - processed
       - states.csv
       - municipios.csv
   - README.md
 
(A estrutura será expandida conforme novas etapas do pipeline forem implementadas.)

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Requests
- JSON
- Pandas (etapas futuras)

## 🔄 Pipeline ETL

### Extração (Extract)
- Consumo da API pública do IBGE
- Coleta dos dados de estados brasileiros
- Armazenamento dos dados brutos em formato JSON (`data/raw/states.json`)

### Transformação (Transform)
- Flatten da hierarquia geográfica do IBGE (município → microrregião → mesorregião → UF)
- Tratamento de registros incompletos (ignora registros sem UF)
- Geração de CSV analítico em `data/processed`

### Carga (Load)
- Etapa futura
- Os dados transformados poderão ser carregados em banco de dados ou data warehouse

## 🚧 Status do Projeto

Em desenvolvimento.

Etapas concluídas:
- Extração de estados brasileiros (JSON)
- Extração de municípios por estado (JSON)
- Transformação de estados (JSON → CSV)
- Transformação de municípios (JSON → CSV)

Próximas etapas:
- Load em banco de dados PostegreSQL
- Extração de dados populacionais por município e ano

