#separando os dados dos rankings do big3 em um arquivo separado

import pandas as pd

csv_players = "data/raw/atp_players.csv"
csv_rankings = "data/clean/atp_rankings_00-20s.csv"

df_players = pd.read_csv(csv_players)
df_rankings = pd.read_csv(csv_rankings)

players = [
    ("Roger", "Federer"),
    ("Rafael", "Nadal"),
    ("Novak", "Djokovic")
]

df_big3 = df_players[
    df_players[["name_first", "name_last"]].apply(tuple, axis=1).isin(players)
]

ids = df_big3["player_id"].tolist()

df_final = df_rankings[df_rankings["player_id"].isin(ids)]

df_final.to_csv("data/clean/big3_rankings.csv", index=False)