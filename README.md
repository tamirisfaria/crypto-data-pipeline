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
DB_NAME=nome_banco
DB_USER=nome_usuario
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

# Integração com Power BI

Coleta os dados:
1. Tive que usar o looker devido a problemas com acesso ao power Bi e utilizar uma ferramentado do site https://console.cloud.timescale.com/dashboard/services/x9ajahmron/overview para conectar o meu banco que esta como local e ser visualizado como remoto.
2. As análises se encontram neste link do looker: [https://lookerstudio.google.com/u/0/reporting/45e894c7-85ef-40ee-80b3-9b341207fcc9/page/75xHF/edit](https://lookerstudio.google.com/reporting/19fffe28-f015-426d-84c2-53620aff8269)
3. Fiz analise no colab: https://colab.research.google.com/drive/1aNV4OOA-MUb5CX1PYiMR9FtkSNr8y8Xu?usp=sharing
