CREATE TABLE IF NOT EXISTS operadoras_ativas (
    id_operadora INT PRIMARY KEY AUTO_INCREMENT,
    registro_ans INT UNIQUE,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_comercializacao INT,
    data_registro DATE
);

CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id_demonstracao INT PRIMARY KEY AUTO_INCREMENT,
    data_registro DATE,
    registro_ans INT,
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras_ativas(registro_ans) ON DELETE CASCADE
);
