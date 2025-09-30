import pandas as pd

#dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_1116135.csv", skiprows=4)

#country Name, code, and 2024 column
df_2024 = df[["Country Name", "Country Code", "2024"]].rename(columns={"2024": "Population (2024)"})

#drop rows without population data
df_2024 = df_2024.dropna(subset=["Population (2024)"])

# cleaned dataset
df_2024.to_csv("population_2024.csv", index=False)

print("Saved population_2024.csv with", len(df_2024), "rows")
