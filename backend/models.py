from pydantic import BaseModel

class Operadora(BaseModel):
    registro_ans: int
    cnpj: str
    razao_social: str
    nome_fantasia: str | None = None
    modalidade: str
    logradouro: str
    numero: str
    complemento: str | None = None
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: str
    telefone: str
    fax: str | None = None
    endereco_eletronico: str
    representante: str
    cargo_representante: str
    regiao_comercializacao: int
    data_registro: str
