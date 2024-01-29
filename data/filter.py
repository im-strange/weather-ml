
import pandas as pd

file = "weather.csv"
df = pd.read_csv(file)
to_keep = ["time", "tavg", "prcp", "wdir", "wspd", "coco"]
df.dropna(axis=1, inplace=True)
to_keep = df.columns

#to_drop = [col for col in df.columns if col not in to_keep]
#df.drop(columns=to_drop, inplace=True)

for col in to_keep[1:]:
    df[col].fillna(df[col].median(), inplace=True)

df.to_csv("weather.csv", index=False)
print("done!")

