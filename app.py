import pandas as pd
import json

data = pd.read_csv('sources/TBD_ASSOS__RS.csv', sep = ';')
data = data[data['Association'].notna()]
data = data[data['Instagram'].notna()]

data = data[['Association', 'Instagram']]

with open('Associations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii = False)