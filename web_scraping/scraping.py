import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL da página
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para salvar os arquivos
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def get_pdf_links():
    """ Extrai os links dos PDFs da página. """
    response = requests.get(URL)
    response.raise_for_status()  # Verifica erros na requisição
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.endswith(".pdf"):
            full_url = requests.compat.urljoin(URL, href)  # Ajusta URL relativa
            pdf_links.append(full_url)
    
    return pdf_links[:2]  # Pegamos apenas os dois primeiros PDFs (Anexo I e II)

def download_pdfs(pdf_links):
    """ Faz o download dos PDFs encontrados. """
    pdf_files = []
    for link in pdf_links:
        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link))
        response = requests.get(link, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        pdf_files.append(filename)
        print(f"Baixado: {filename}")
    
    return pdf_files

def create_zip(files):
    """ Compacta os arquivos baixados em um único ZIP. """
    zip_path = os.path.join(DOWNLOAD_DIR, "anexos.zip")
    with ZipFile(zip_path, "w") as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    print(f"Arquivos compactados em: {zip_path}")

# Execução
pdf_links = get_pdf_links()
if pdf_links:
    pdf_files = download_pdfs(pdf_links)
    create_zip(pdf_files)
else:
    print("Nenhum PDF encontrado.")
