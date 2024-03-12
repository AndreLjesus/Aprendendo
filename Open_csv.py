import pandas as pd

#Print .CSV as string
df = pd.read_csv("archive.csv")
print(df.to_string())

