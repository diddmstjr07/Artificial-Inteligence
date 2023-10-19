import pandas as pd

df = pd.read_csv('result_2023-10-13 15:33:11.csv', index_col=0)
value = df.iloc[1, 1]
print(value)