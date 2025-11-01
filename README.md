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
### 🗂️ Data Flow

1. **Extraction:** Data collected from CSV files, APIs, or simulated data generators.  
2. **Transformation:** Data cleaning, normalization, and enrichment using Python and SQL.  
3. **Loading:** Processed data stored in Snowflake, partitioned by date and category.  
4. **Analytics:** Creation of summary tables and visual dashboards.

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
├── data/              # Sample input data
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


## 🇧🇷 Versão em Português

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

1. **Extração:** dados coletados de arquivos CSV, APIs ou geradores simulados.  
2. **Transformação:** limpeza, normalização e enriquecimento dos dados usando Python e SQL.  
3. **Carga:** dados processados armazenados no Snowflake, particionados por data e categoria.  
4. **Análise:** criação de tabelas resumo e dashboards visuais.

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
├── data/               # Dados de entrada
├── sql/                # Consultas e transformações SQL
├── notebooks/          # Análises exploratórias
├── docker/             # Arquivos de configuração do Docker
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências
```
---
### 💡 Objetivo

Demonstrar **habilidades completas em engenharia de dados** — da ingestão à visualização — usando ferramentas reais e boas práticas do mercado.
