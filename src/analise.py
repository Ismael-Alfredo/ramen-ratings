import pandas as pd

df = pd.read_csv("../data/ramen-ratings.csv", index_col=0)

print(df.head())