import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ans_dados"
)
cursor = conn.cursor()

df = pd.read_csv("../data/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")
df = df.fillna("")  # Substitui valores NaN por strings vazias

# Query para inserir os dados
sql = """INSERT INTO operadoras_ativas (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro,
          numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico,
          representante, cargo_representante, regiao_comercializacao, data_registro)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Inserir em lote para melhor performance
cursor.executemany(sql, [tuple(map(str, row)) for _, row in df.iterrows()])
conn.commit()

cursor.close()
conn.close()
