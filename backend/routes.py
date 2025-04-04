from backend.models import Operadora
from typing import List
from fastapi import APIRouter, Query
import mysql.connector
from datetime import date

router = APIRouter()

@router.get("/buscar", response_model=List[Operadora])
def buscar_operadoras(q: str = Query(..., description="Texto para busca")):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="ans_dados"
    )
    cursor = conn.cursor()

    query = """
    SELECT * FROM operadoras_ativas 
    WHERE razao_social LIKE %s 
       OR nome_fantasia LIKE %s 
       OR cidade LIKE %s 
    LIMIT 10;
    """
    cursor.execute(query, (f"%{q}%", f"%{q}%", f"%{q}%"))
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    # Ajustar os dados para os tipos esperados pelo Pydantic
    results = []
    for row in rows:
        data = dict(zip(columns, row))

        # Converte o campo 'data_registro' de datetime.date para string
        if data.get('data_registro') and isinstance(data['data_registro'], date):
            data['data_registro'] = data['data_registro'].strftime('%Y-%m-%d')

        # Verifica e converte os campos numéricos que podem ser None
        if data.get('ddd') is None:
            data['ddd'] = ''
        if data.get('telefone') is None:
            data['telefone'] = ''
        if data.get('fax') is None:
            data['fax'] = ''
        if data.get('regiao_comercializacao') is None:
            data['regiao_comercializacao'] = 0

        results.append(Operadora(**data))

    cursor.close()
    conn.close()
    return results
