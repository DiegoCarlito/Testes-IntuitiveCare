import os
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ans_dados"
)
cursor = conn.cursor()

# Desabilita constraints temporariamente
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

# Diretório padrão com CSVs
data_dir = "../data/demonstracoes_contabeis"

csv_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".csv")]

# Processa cada arquivo
for file_path in csv_files:
    print(f"Processando: {file_path}")
    df = pd.read_csv(file_path, delimiter=";", encoding="utf-8")
    df = df.fillna("")

    # Conversões
    df["VL_SALDO_INICIAL"] = df["VL_SALDO_INICIAL"].astype(str).str.replace(",", ".").astype(float)
    df["VL_SALDO_FINAL"] = df["VL_SALDO_FINAL"].astype(str).str.replace(",", ".").astype(float)
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce").dt.date

    # Query SQL
    sql = """
    INSERT INTO demonstracoes_contabeis 
    (data_registro, registro_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in df.itertuples(index=False, name=None):
        try:
            cursor.execute(sql, row)
        except mysql.connector.Error as e:
            print(f"Erro ao inserir linha {row}: {e}")

    conn.commit()
    print(f"Arquivo {file_path} inserido com sucesso.\n")

cursor.close()
conn.close()
