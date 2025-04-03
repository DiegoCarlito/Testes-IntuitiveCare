import pdfplumber
import pandas as pd
import zipfile
import os

# Caminho do PDF
pdf_path = "downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_path = "downloads/rol_procedimentos.csv"
zip_path = "downloads/Teste_Diego_Carlito_Rodrigues_de_Souza.zip"

# Substituições das abreviações
substituicoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

# Cabeçalho esperado
cabecalho_oficial = ["Procedimento", "RN", "Vigência", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "Subgrupo", "Grupo", "Capítulo"]

# Função para verificar se uma linha é um cabeçalho repetido
def eh_cabecalho_repetido(linha):
    return all(any(str(c).lower() in str(l).lower() for c in cabecalho_oficial) for l in linha)

# Função para extrair tabelas do PDF
def extrair_tabela(pdf_path):
    dados = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages[2:]:  # Ignorando as duas primeiras páginas
            tabelas = page.extract_tables()
            for tabela in tabelas:
                for linha in tabela:
                    if eh_cabecalho_repetido(linha):  # Pula cabeçalhos repetidos
                        continue
                    if any(linha):  # Evita linhas vazias
                        dados.append(linha)
    
    return dados

# Extrai os dados sem cabeçalhos repetidos
dados_extraidos = extrair_tabela(pdf_path)

# Criar DataFrame e ajustar colunas
df = pd.DataFrame(dados_extraidos, columns=cabecalho_oficial)

# Substituir abreviações
df.replace(substituicoes, inplace=True)

# Salvar como CSV
df.to_csv(csv_path, index=False, encoding="utf-8")

# Compactar o CSV em ZIP
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

print(f"Arquivo CSV salvo e compactado em: {zip_path}")
