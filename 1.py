import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with actual path after downloading
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Preview the dataset
print(df.head())

# Sort by population in 2022
df_top = df[['Country Name', '2022']].dropna().sort_values(by='2022', ascending=False).head(10)

# Plot
plt.figure(figsize=(12,6))
sns.barplot(x='2022', y='Country Name', data=df_top, palette='coolwarm')
plt.xlabel("Population in 2022")
plt.ylabel("Country")
plt.title("Top 10 Most Populous Countries (2022)")
plt.tight_layout()
plt.show()

