import pandas as pd

paraules = pd.read_csv("paraules_tematica_penjat.csv")

paraules_dict = paraules.to_dict(orient='list')

print(paraules_dict)