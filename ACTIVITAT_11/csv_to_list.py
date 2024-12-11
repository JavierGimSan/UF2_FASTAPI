import pandas as pd
import insert_data as ins_dat

def csv_to_json():
    paraules = pd.read_csv("paraules_tematica_penjat.csv")

    paraules_dict = paraules.to_dict(orient='list')

    return paraules_dict

    # print(paraules_dict["WORD"][0])
    # print(paraules_dict["THEME"][0])

data = csv_to_json()

for i in range (500):
    ins_dat.insert_dat_csv_to_db(i, data) # Pilla la función del archivo 'insert_data.py' y la hace 500 veces, que son los elementos que tiene la lista