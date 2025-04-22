# Crypto Data Collector

Este projeto consome dados da API pública [CoinCap](https://docs.coincap.io/) sobre criptomoedas e armazena essas informações em um banco de dados PostgreSQL relacional.

Você pode usar os dados para análise posterior em ferramentas como Power BI, Metabase, etc.

# Funcionalidades

Coleta informações das principais criptomoedas do mercado.
Armazena o preço, capitalização de mercado e volume em USD
Usa PostgreSQL como banco de dados

# Requisitos

- Python 3.8+
- PostgreSQL instalado e rodando
- pip ou virtualenv para gerenciamento de pacotes

# Configuração

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo .env na raiz do projeto com os dados de acesso ao banco de dados PostgreSQL e a chave da API:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_db
DB_USER=crypto_user
DB_PASSWORD=minha_senha
API_KEY=chave_api
```

# Execução
Para coletar os dados e salvar no banco:

```bash
python main.py
```

Se tudo estiver correto, você verá:

```bash
Dados inseridos com sucesso.
```