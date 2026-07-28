import pandas as pd

df = pd.read_csv("nba_player_stats_2026.csv")

print("Shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types and missing values:")
print(df.info())

print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate player names:", df["PLAYER"].duplicated().sum())

top_scorers = df.sort_values("PTS", ascending=False).head(10).reset_index(drop=True)
top_scorers.index += 1
print("\nTop 10 scorers:")
print(top_scorers[["PLAYER", "TEAM", "PTS"]])