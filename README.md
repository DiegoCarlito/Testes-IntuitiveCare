# Testes de Nivelamento da Intuitivecare

Este repositório contém a implementação dos testes de nivelamento da Intuitivecare, abordando Web Scraping, Transformação de Dados, Banco de Dados e Desenvolvimento de API.

## 1. TESTE DE WEB SCRAPING

### Objetivo
Desenvolver um script em Python ou Java para realizar as seguintes tarefas:

1. Acessar o site: [ANS - Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
2. Fazer o download dos Anexos I e II em formato PDF.
3. Compactar os arquivos baixados em um único arquivo ZIP ou RAR.

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS

### Objetivo
Criar um script em Python ou Java que execute as seguintes tarefas:

1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I do teste 1 (todas as páginas).
2. Salvar os dados extraídos em um arquivo CSV estruturado.
3. Compactar o arquivo CSV em um ZIP denominado `Teste_{seu_nome}.zip`.
4. Substituir as abreviações das colunas OD e AMB por suas descrições completas, conforme a legenda no rodapé.

## 3. TESTE DE BANCO DE DADOS

### Objetivo
Criar scripts SQL compatíveis com MySQL 8+ ou PostgreSQL >10.0 para executar as seguintes tarefas:

### Preparação
1. Baixar os arquivos dos últimos 2 anos do repositório público:
   - [Demonstrações Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
2. Baixe os Dados cadastrais das Operadoras Ativas na ANS no formato CSV em:
   - [Dados cadastrais das Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

### Tarefas de Código
3. Criar queries para estruturar tabelas necessárias para o arquivo csv.
4. Elaborar queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.
5. Desenvolver uma query analítica para responder:
   - Quais as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR" no último trimestre?
   - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

## 4. TESTE DE API

### Objetivo
Desenvolver uma interface web utilizando Vue.js e um servidor em Python para realizar as tarefas abaixo.

### Tarefas de Código
1. Utilizar o CSV do item 3.2. para alimentar a API.
2. Criar um servidor com uma rota que permita realizar buscas textuais na lista de cadastros de operadoras e retornar os registros mais relevantes.
3. Elaborar uma coleção no Postman para demonstrar o resultado.

## Tecnologias Utilizadas
- **Python** (para Web Scraping e Transformação de Dados)
- **MySQL 8+** / **PostgreSQL 10+** (para Banco de Dados)
- **Vue.js** (para a interface web)
- **Postman** (para testes de API)

## Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu_usuario/Testes-IntuitiveCare.git
cd Testes-IntuitiveCare
```

### 2. Configure o ambiente Python
Crie e ative um ambiente virtual, e instale as dependências:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Teste 1 - Web Scraping

Execute o script de scraping:
```bash
python3 web_scraping/scraping.py
```
Os arquivos PDF e o arquivo compactado `.zip` serão salvos na pasta `downloads/`.

---

### 4. Teste 2 - Transformação de Dados

Antes de executar este teste, certifique-se de ter rodado o **Teste 1**, pois ele gera o PDF necessário.

```bash
python3 data_transformation/extract_table.py
```

O resultado será um arquivo CSV estruturado e compactado no formato `Teste_Diego_Carlito_Rodrigues_de_Souza.zip`, salvo na pasta `downloads/`.

---

### 5. Teste 3 - Banco de Dados

#### Subindo o banco com Docker:
```bash
cd database
docker-compose up --build
```

#### Populando as tabelas:
```bash
cd scripts
python3 populate_operadoras.py
python3 populate_despesas.py
```

#### Acessando o banco MySQL manualmente:
```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```
> **Senha:** `1234`

#### Consultas analíticas:

**Top 10 operadoras com maiores despesas no último trimestre (2024 Q4):**
```sql
SELECT 
    oa.razao_social,
    dc.registro_ans,
    SUM(dc.vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.registro_ans = oa.registro_ans
WHERE 
    dc.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%HOSPITALAR%' AND
    dc.data_registro BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY dc.registro_ans, oa.razao_social
ORDER BY total_despesa DESC
LIMIT 10;
```

**Top 10 operadoras com maiores despesas no ano de 2023:**
```sql
SELECT 
    oa.razao_social,
    dc.registro_ans,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesa
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.registro_ans = oa.registro_ans
WHERE 
    dc.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS%HOSPITALAR%' AND
    dc.data_registro BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY dc.registro_ans, oa.razao_social
ORDER BY total_despesa DESC
LIMIT 10;
```

Perfeito! Aqui está o **passo 6** com as observações adicionais que você pediu, incluindo a dependência do passo 3 (banco de dados) e como rodar o frontend:

---

### 6. Teste 4 - API

> ⚠️ **Pré-requisito:** Certifique-se de ter executado o **Teste 3** para que as tabelas do banco estejam populadas com os dados corretos.

#### Subindo o servidor FastAPI:
```bash
uvicorn api.server:app --reload
```

> A API estará disponível em: `http://127.0.0.1:8000`

#### Testando com o Postman:
1. Abra o Postman.
2. Clique em **Import** e selecione o arquivo `api/postman_collection.json`.
3. Vá até a aba **Collections** e clique na coleção importada.
4. Execute a requisição **amil** (`GET localhost:8000/api/buscar?q=amil`).
5. Você verá os dados retornados da API.

> Dica: altere o parâmetro `query` na URL para testar outras operadoras, como `unimed`, `bradesco`, etc.

#### Rodando o frontend (Vue.js):
```bash
cd frontend
npm install
npm run serve
```

> A interface web estará disponível em: `http://localhost:8080`

## Contato
Para mais informações, entre em contato pelo e-mail: `diego.carlito01@gmail.com`.

<hr>
<div style="text-align: center; margin-top: 40px;">
  <img src="https://github.com/DiegoCarlito.png" 
       alt="Foto de Diego Carlito" 
       style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
  <p style="margin-top: 10px; font-weight: bold;">Diego Carlito Rodrigues de Souza</p>
</div>
