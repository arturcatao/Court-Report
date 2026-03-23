import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Court Report")
st.write("Dashboard do Big3")


CSV = "data/processed/big3_rankings.csv"
df = pd.read_csv(CSV)

df = df[df["rank"] <= 100]
df["ranking_date"] = pd.to_datetime(df["ranking_date"])

fig, ax = plt.subplots(figsize=(10, 6))

colors = {
    "Federer": "green", # grass
    "Nadal": "red", # clay
    "Djokovic": "blue" # hardcourt
}

for player in df["name_last"].unique():
    sub = df[df["name_last"] == player].sort_values("ranking_date")
    
    ax.plot(
        sub["ranking_date"],
        sub["rank"],
        label=player,
        linewidth=2,
        color = colors.get(player, "black")
    )

ax.set_xlabel("Data")
ax.set_ylabel("Rank")
ax.set_title("Ranking do BIG3 ao longo do tempo")

ax.invert_yaxis()

ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

# /-/-/-/-/

CSV = "data/processed/big3_matches.csv"
df = pd.read_csv(CSV)

# categorias no eixo x
categorias = ["clay", "grass", "hard"]
x = range(len(categorias))

width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

colors = {
    "Federer": "green", # grass
    "Nadal": "red", # clay
    "Djokovic": "blue" # hardcourt
}

# barras para cada jogador
for i, (_, row) in enumerate(df.iterrows()):
    valores = [row["clay"], row["grass"], row["hard"]]
    
    posicoes = [pos + (i - 1)*width for pos in x]
    
    ax.bar(
        posicoes,
        valores,
        width=width,
        label=row["name_last"],
        color=colors.get(row["name_last"], "black")
    )
    
    for j, v in enumerate(valores):
        ax.text(
            posicoes[j],
            v + 0.005,              # ajusta altura do texto
            f"{v*100:.0f}%",        # porcentagem
            ha="center",
            va="bottom",
            fontsize=9
        )

# labels
ax.set_xticks(x)
ax.set_xticklabels(["Clay", "Grass", "Hard"])
ax.set_ylabel("Winrate")
ax.set_xlabel("Superfície")
ax.set_title("Winrate do Big3 por Superfície")

ax.legend()
ax.grid(axis="y", alpha=0.3)

ax.set_ylim(0.6, 1.0)

plt.tight_layout()
st.pyplot(fig)