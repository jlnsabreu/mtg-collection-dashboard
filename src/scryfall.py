import pandas as pd
from pathlib import Path
import requests
import time

def query_data():
    collection = Path('data/processed/cleaned_collection.csv')
    df = pd.read_csv(collection)
    return df

def chunks(lst, size = 75):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def get_scryfall_data():
    url = 'https://api.scryfall.com/cards/collection'

    headers = {'User-Agent':'MTGCollectionDashboard/1.0', 'Content-Type': 'application/json'}

    ids = query_data()['scryfall_id'].dropna().unique()
    identifiers = [{'id': id} for id in ids]

    all_data = []

    for chunk in chunks(identifiers):
        payload = {'identifiers': chunk}

        r = requests.post(
            url, json=payload,headers=headers)
        
        print(r.status_code)

        if r.status_code == 200:
            data = r.json()
            all_data.extend(data['data'])
        else:
            print(f"Error: {r.status_code}", r.text)
        
        time.sleep(0.1)
    
    df = pd.DataFrame(all_data)

    output_dir = Path('data/processed/scryfall_data.csv')
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_dir, index=False)

    return df

def merge():
    scryfall_data = pd.read_csv('data/processed/scryfall_data.csv')
    collection = pd.read_csv('data/processed/cleaned_collection.csv')

    merged_df = collection.merge(scryfall_data, left_on='scryfall_id', right_on='id', how='left')

    output_dir = Path('data/processed/merged_collection.csv')
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    merged_df.to_csv(output_dir, index=False)

    return merged_df