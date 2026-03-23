# Court Report

Dashboard interativo de análise histórica do Big3 do tênis (Roger Federer, Rafael Nadal e Novak Djokovic), construído com Python e Streamlit.

> Este projeto foi desenvolvido exclusivamente para fins de aprendizado das tecnologias utilizadas. Não tem fins comerciais.

Decidi começar a explorar as principais tecnologias da área de ciência de dados. Ao pesquisar fontes de dados públicas, encontrei o repositório do Jeff Sackmann com um histórico completo de partidas e rankings do circuito ATP. Como acompanho tênis há bastante tempo, pareceu natural usar esse dataset como base para o estudo, o que tornou o aprendizado mais interessante do que trabalhar com dados genéricos.

---

## Análises

- **Evolução do ranking** : comportamento do ranking dos três jogadores de 2000 a 2024
- **Winrate por superfície** : percentual de vitórias em saibro, grama e quadra dura

---

## Tecnologias

- Python 3.12
- pandas
- matplotlib
- Streamlit

---

## Estrutura do projeto

```
Court-Report/
├── data/
│   ├── raw/          # Dados originais (não versionados)
│   └── clean/        # Dados processados (não versionados)
├── notebooks/        # Notebooks de limpeza e exploração
├── src/              # Scripts e dashboard
│   └── app.py        # Dashboard Streamlit
├── .gitignore
└── README.md
```

---

## Como rodar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Court-Report.git
cd Court-Report

# Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install streamlit pandas matplotlib

# Rode o dashboard
streamlit run src/app.py
```

---

## Dados

Os dados de partidas e rankings utilizados neste projeto são provenientes do repositório público de **Jeff Sackmann**:

> [github.com/JeffSackmann/tennis_atp](https://github.com/JeffSackmann/tennis_atp)

Os dados são disponibilizados sob a licença [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/). Todo o crédito pelos dados pertence ao autor original.

---

## Autor

Desenvolvido por **Artur Catão** como projeto pessoal de aprendizado — 4º período de Ciência da Computação, UFCG.