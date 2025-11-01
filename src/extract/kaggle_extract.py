import os

# cria pasta se não existir
os.makedirs("data/raw", exist_ok=True)

# baixa e descompacta o dataset
os.system("kaggle datasets download -d mmohaiminulislam/ecommerce-data-analysis -p data/raw --unzip")
