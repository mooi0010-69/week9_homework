import pandas as pd
import pycountry

df = pd.read_csv("population_2024.csv")

#convert codes to numeric codes 
def letter_to_numeric(letter):
    try:
        return int(pycountry.countries.get(alpha_3=letter).numeric)
    except:
        return None

#convery
df["Country Numeric"] = df["Country Code"].apply(letter_to_numeric)

#drop rows where conversion failed (NaN in Country Numeric)
df_clean = df.dropna(subset=["Country Numeric"])

#drop the original Country Code column
df_clean = df_clean.drop(columns=["Country Code"])

#save cleaned CSV
df_clean.to_csv("population_2024_cleaned2.csv", index=False)

print("done")
