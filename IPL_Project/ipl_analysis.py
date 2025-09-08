import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("match_data.csv")

# Preview
print("Dataset Preview:")
print(df.head())

# Top run scorers
top_scorers = df.groupby("Player")["Runs"].sum().sort_values(ascending=False).head(5)
print("\nTop Run Scorers:\n", top_scorers)

# Top wicket takers
top_bowlers = df.groupby("Player")["Wickets"].sum().sort_values(ascending=False).head(5)
print("\nTop Wicket Takers:\n", top_bowlers)

# Team performance (total runs per team)
team_runs = df.groupby("Team")["Runs"].sum()

# Plotting top scorers
plt.figure(figsize=(8,5))
top_scorers.plot(kind="bar", color="skyblue")
plt.title("Top 5 Run Scorers")
plt.xlabel("Player")
plt.ylabel("Total Runs")
plt.show()

# Plotting team runs
plt.figure(figsize=(8,5))
team_runs.plot(kind="pie", autopct="%1.1f%%")
plt.title("Team Contribution by Runs")
plt.ylabel("")
plt.show()
