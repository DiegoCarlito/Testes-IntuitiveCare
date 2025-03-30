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
- **Python** / **Java** (para Web Scraping e Transformação de Dados)
- **MySQL 8+** / **PostgreSQL 10+** (para Banco de Dados)
- **Vue.js** (para a interface web)
- **Postman** (para testes de API)

## Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu_usuario/Testes-IntuitiveCare.git
   cd Testes-IntuitiveCare
   ```
2. Siga as instruções de cada diretório correspondente a cada teste para execução.

## Contato
Para mais informações, entre em contato pelo e-mail: `diego.carlito01@gmail.com`.

