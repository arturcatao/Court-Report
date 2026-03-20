import pandas as pd
import matplotlib.pyplot as plt

CSV = "data/clean/big3_rankings.csv"
df = pd.read_csv(CSV)

players = ["Federer", "Nadal", "Djokovic"]

df = df[df["rank"] <= 100]

plt.figure(figsize=(10, 6))

for player in df["name_last"].unique():
    sub = df[df["name_last"] == player].sort_values("ranking_date")
    
    plt.plot(
        sub["ranking_date"],
        sub["rank"],
        label=player,
        linewidth=2
    )

plt.xlabel("Data")
plt.ylabel("Rank")
plt.title("Ranking ao longo do tempo")

plt.gca().invert_yaxis()

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()