import pandas as pd
import matplotlib.pyplot as plt

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

df["PTS_PER_MIN"] = df["PTS"] / df["MIN"]

most_efficient = df.sort_values("PTS_PER_MIN", ascending=False).head(10).reset_index(drop=True)
most_efficient.index += 1

print("\nTop 10 most efficient scorers (points per minute):")
print(most_efficient[["PLAYER", "TEAM", "PTS", "MIN", "PTS_PER_MIN"]])

qualified = df[df["MIN"] > 500]

df["PTS_PER_MIN"] = qualified["PTS"] / qualified["MIN"]

most_efficient = qualified.sort_values("PTS_PER_MIN", ascending=False).head(10).reset_index(drop=True)
most_efficient.index += 1

print("\nTop 10 most efficient scorers (min. 500 minutes played):")
print(most_efficient[["PLAYER", "TEAM", "PTS", "MIN", "PTS_PER_MIN"]])

team_efficiency = df.groupby("TEAM")["EFF"].mean().sort_values(ascending=False)

print("\nAverage player efficiency (EFF) by team:")
print(team_efficiency.head(10))

plt.figure()
plt.scatter(df["MIN"], df["PTS"], alpha=0.5)
plt.title("Minutes Played vs. Points Scored")
plt.xlabel("Minutes Played")
plt.ylabel("Points Scored")
plt.tight_layout()
plt.savefig("minutes_vs_points.png")
print("\nScatter plot saved as minutes_vs_points.png")