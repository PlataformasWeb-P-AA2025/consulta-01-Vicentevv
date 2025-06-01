import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["datos_excel"]
collection = db["registros"]

# Lectura de archivos Excel
archivos = ["2022.xlsx", "2023.xlsx"]
for archivo in archivos:
    df = pd.read_excel(archivo)
    data = df.to_dict(orient="records")
    collection.insert_many(data)

# Consultas
print("Consulta 1: Total de documentos:")
print(collection.count_documents({}))

print("Consulta 2: Un registro de ejemplo:")
print(collection.find_one())
