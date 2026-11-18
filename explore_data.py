import pandas as pd

df = pd.read_excel("orders_anonymized.xlsx")
print(df.head(5))
print("\nRows:", len(df))
print("Platforms:", df["Platform"].unique())
