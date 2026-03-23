import pandas as pd
import matplotlib.pyplot as plt

CSV = "data/processed/big3_rankings.csv"
df = pd.read_csv(CSV)

df = df[df["rank"] <= 100]
df["ranking_date"] = pd.to_datetime(df["ranking_date"])

plt.figure(figsize=(10, 6))

colors = {
    "Federer": "green", # grass
    "Nadal": "red", # clay
    "Djokovic": "blue" # hardcourt
}

for player in df["name_last"].unique():
    sub = df[df["name_last"] == player].sort_values("ranking_date")
    
    plt.plot(
        sub["ranking_date"],
        sub["rank"],
        label=player,
        linewidth=2,
        color = colors.get(player, "black")
    )

plt.xlabel("Data")
plt.ylabel("Rank")
plt.title("Ranking do BIG3 ao longo do tempo")

plt.gca().invert_yaxis()

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("static/big3_rank.png", dpi=150)
plt.show()