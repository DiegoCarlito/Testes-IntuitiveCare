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
df = df.replace({pd.NA: None, pd.NaT: None, float('nan'): None})

# Preencher valores vazios com None para colunas numéricas
df["Regiao_de_Comercializacao"] = df["Regiao_de_Comercializacao"].replace("", None)
df["Data_Registro_ANS"] = pd.to_datetime(df["Data_Registro_ANS"], errors="coerce").dt.date

# Substitui NaN por None no geral
df = df.where(pd.notnull(df), None)

sql = """INSERT INTO operadoras_ativas 
    (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro,
     numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, 
     endereco_eletronico, representante, cargo_representante, 
     regiao_comercializacao, data_registro)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Inserir no banco
for _, row in df.iterrows():
    cursor.execute(sql, tuple(row))

conn.commit()
cursor.close()
conn.close()
