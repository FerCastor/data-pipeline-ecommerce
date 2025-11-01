# 🛒 Online Sales Data Pipeline

## 🇺🇸 English Version

### 📘 Project Overview
This project simulates a complete **data engineering pipeline** for an **e-commerce platform**, covering data extraction, transformation, loading (ETL), and analysis.  
The goal is to build a robust and scalable pipeline capable of transforming raw sales data into valuable business insights.

---

### 🚀 Architecture

**Components:**
- **Python:** used for data extraction, transformation, and loading (ETL scripts)  
- **Airflow:** orchestration of ETL tasks  
- **Snowflake:** cloud data warehouse for structured storage and analytics  
- **Docker:** containerized environment for local development and deployment  
- **Bitbucket / GitHub:** version control and CI/CD integration  
- **Power BI / Tableau (optional):** for dashboards and data visualization  

---

### 📞 Data Flow

1. **Extraction:** Data collected from CSV files, APIs, or Kaggle datasets via Kaggle API.  
2. **Transformation:** Data cleaning, normalization, and enrichment using Python and SQL.  
3. **Loading:** Processed data stored in Snowflake, partitioned by date and category.  
4. **Analytics:** Creation of summary tables and visual dashboards.

---

### 📌 Data Extraction via Kaggle API

To run the extraction script, the user must:

1. Create a Kaggle account.  
2. Generate an API token (`kaggle.json`) in your Kaggle account settings.  
3. Place `kaggle.json` in the appropriate location:  
   - `~/.kaggle/` on Linux/macOS  
   - `C:\Users\<user>\.kaggle\` on Windows  
4. Install the Kaggle Python package:

```bash
pip install kaggle
```

5. Run the extraction script:

```bash
python scripts/extract_kaggle.py
```

> The script downloads the dataset and saves it in `data/raw/`.  
> **Important:** Do not commit `kaggle.json` to GitHub.

After extraction, processed and cleaned data is saved in `data/processed/` for further analysis.

---

### 📊 Example Insights

- Total revenue by product category  
- Top 10 best-selling products  
- Average order value per customer segment  
- Monthly sales growth rate  

---

### ⚙️ Technologies Used

- Python 3.10+  
- Snowflake  
- Apache Airflow  
- Docker  
- Bitbucket / GitHub  
- Pandas, SQLAlchemy, Requests  

---

### 🧱 Repository Structure
```
online-sales-pipeline/
│
├── dags/              # Airflow DAGs
├── scripts/           # Python ETL scripts
├── data/              # Input data
│   ├── raw/           # Raw datasets (from Kaggle/API)
│   └── processed/     # Cleaned and transformed data
├── sql/               # SQL queries and transformations
├── notebooks/         # Exploratory analysis
├── docker/            # Docker configuration files
├── README.md          # Project documentation
└── requirements.txt   # Dependencies
```

---

### 💡 Goal

To demonstrate end-to-end **data engineering skills** — from ingestion to visualization — using real-world tools and best practices.

---

## 🇷🇷 Versão em Português

### 📘 Visão Geral do Projeto
Este projeto simula um **pipeline completo de engenharia de dados** para uma **plataforma de e-commerce**, cobrindo as etapas de extração, transformação, carga (ETL) e análise.  
O objetivo é construir um pipeline robusto e escalável que transforme dados brutos de vendas em **insights de negócio valiosos**.

---

### 🚀 Arquitetura

**Componentes:**
- **Python:** extração, transformação e carga de dados (ETL)  
- **Airflow:** orquestração das tarefas  
- **Snowflake:** armazenamento e análise dos dados estruturados  
- **Docker:** ambiente containerizado para desenvolvimento e deploy  
- **Bitbucket / GitHub:** controle de versão e CI/CD  
- **Power BI / Tableau (opcional):** visualização dos dados  

---

### 🗂️ Fluxo de Dados

1. **Extração:** dados coletados de arquivos CSV, APIs ou datasets do Kaggle via API.  
2. **Transformação:** limpeza, normalização e enriquecimento dos dados usando Python e SQL.  
3. **Carga:** dados processados armazenados no Snowflake, particionados por data e categoria.  
4. **Análise:** criação de tabelas resumo e dashboards visuais.

---

### 📌 Extração de Dados via API do Kaggle

Para rodar o script de extração, o usuário deve:

1. Criar uma conta no Kaggle.  
2. Gerar um token de API (`kaggle.json`) nas configurações da conta.  
3. Colocar `kaggle.json` no local correto:  
   - `~/.kaggle/` no Linux/macOS  
   - `C:\Users\<usuário>\.kaggle\` no Windows  
4. Instalar o pacote Python do Kaggle:

```bash
pip install kaggle
```

5. Rodar o script de extração:

```bash
python scripts/extract_kaggle.py
```

> O script baixa o dataset e salva em `data/raw/`.  
> **Importante:** não envie `kaggle.json` para o GitHub.

Após a extração, os dados processados e limpos são salvos em `data/processed/` para análise posterior.

---

### 📊 Exemplos de Insights

- Receita total por categoria de produto  
- Top 10 produtos mais vendidos  
- Ticket médio por segmento de cliente  
- Crescimento mensal de vendas  

---

### ⚙️ Tecnologias Utilizadas

- Python 3.10+  
- Snowflake  
- Apache Airflow  
- Docker  
- Bitbucket / GitHub  
- Pandas, SQLAlchemy, Requests  

---

### 🧱 Estrutura do Repositório
```
online-sales-pipeline/
│
├── dags/               # DAGs do Airflow
├── scripts/            # Scripts ETL em Python
├── data/              # Dados de entrada
│   ├── raw/           # Datasets brutos (do Kaggle/API)
│   └── processed/     # Dados limpos e transformados
├── sql/               # Consultas e transformações SQL
├── notebooks/         # Análises exploratórias
├── docker/            # Arquivos de configuração do Docker
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências
```

---

### 💡 Objetivo

Demonstrar **habilidades completas em engenharia de dados** — da ingestão à visualização — usando ferramentas reais e boas práticas do mercado.

