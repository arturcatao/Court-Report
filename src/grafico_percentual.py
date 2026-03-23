import pandas as pd
import matplotlib.pyplot as plt

CSV = "data/processed/big3_matches.csv"
df = pd.read_csv(CSV)

# categorias no eixo x
categorias = ["clay", "grass", "hard"]
x = range(len(categorias))

width = 0.25

plt.figure(figsize=(10, 6))

colors = {
    "Federer": "green", # grass
    "Nadal": "red", # clay
    "Djokovic": "blue" # hardcourt
}

# barras para cada jogador
for i, (_, row) in enumerate(df.iterrows()):
    valores = [row["clay"], row["grass"], row["hard"]]
    
    posicoes = [pos + (i - 1)*width for pos in x]
    
    plt.bar(
        posicoes,
        valores,
        width=width,
        label=row["name_last"],
        color=colors.get(row["name_last"], "black")
    )
    
    for j, v in enumerate(valores):
        plt.text(
            posicoes[j],
            v + 0.005,              # ajusta altura do texto
            f"{v*100:.0f}%",        # porcentagem
            ha="center",
            va="bottom",
            fontsize=9
        )

# labels
plt.xticks(x, ["Clay", "Grass", "Hard"])
plt.ylabel("Winrate")
plt.xlabel("Superfície")
plt.title("Winrate do Big3 por Superfície")

plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.ylim(0.6, 1.0)

plt.tight_layout()
plt.savefig("static/percentual_vit.png", dpi=150)
plt.show()