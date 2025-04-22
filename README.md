# 📊 Crypto Data Collector

Este projeto consome dados da API pública [CoinCap](https://docs.coincap.io/) sobre criptomoedas e armazena essas informações em um banco de dados PostgreSQL relacional.

Você pode usar os dados para análise posterior em ferramentas como Power BI, Metabase, etc.

---

## 🚀 Funcionalidades

- Coleta as principais criptomoedas do mercado (nome, símbolo, rank)
- Armazena o preço, capitalização de mercado e volume em USD
- Usa PostgreSQL como banco de dados
- Variáveis de configuração por `.env`
- Estrutura modular e clara com boas práticas

---

## 📦 Requisitos

- Python 3.8+
- PostgreSQL instalado e rodando
- pip ou virtualenv para gerenciamento de pacotes

---