import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("covid_data.csv")

# Basic info
print("Dataset Preview:")
print(df.head())

# Total cases by country
cases_by_country = df.groupby("Country")["Cases"].sum()
print("\nTotal Cases by Country:\n", cases_by_country)

# Growth rate calculation using numpy
df["Daily_Growth"] = df.groupby("Country")["Cases"].diff().fillna(0)
print("\nWith Daily Growth:\n", df.head())

# Visualization
plt.figure(figsize=(10,6))
for country in df["Country"].unique():
    country_data = df[df["Country"] == country]
    plt.plot(country_data["Date"], country_data["Cases"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Cases Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
