import pandas as pd

data = pd.read_csv("french_words.csv")
data_list = data.to_dict(orient="records")
df = pd.DataFrame(data_list)
print(df)