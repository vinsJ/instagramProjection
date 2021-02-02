import pandas as pd
import json

def getLinks():
    data = pd.read_csv('sources/TBD_ASSOS__RS.csv', sep = ';')
    data = data[data['Association'].notna()]
    data = data[data['Instagram'].notna()]

    data = data[['Association', 'Instagram']]

    return data 

# Save pandas matrix as json (have to replace '\' manually in .json)
def saveLinksIntoJson(data):
    with open('Associations.json', 'w', encoding='utf-8') as f:
        data.to_json(f, force_ascii = False, orient = 'records')