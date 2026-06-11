import pandas as pd
from pathlib import Path

def load_data() -> list[pd.DataFrame]:
    data = Path('data/raw')
    dfs = [pd.read_csv(file) for file in data.iterdir() if file.is_file() and file.suffix == ".csv"]
    return dfs
    
    
def cleanup (dfs: list[pd.DataFrame]) -> pd.DataFrame:

    cols = ['name', 'quantity', 'rarity', 'set_code', 'set_name', 'foil','scryfall_id', 'condition', 'language']

    cleaned_dfs = []

    for df in dfs:
        df.columns = df.columns.str.lower().str.replace(' ', '_').str.strip()
        df = df[[col for col in cols if col in df.columns]]
        cleaned_dfs.append(df)
        
    cleaned_df = pd.concat(cleaned_dfs, ignore_index=True)
    
    output_dir = Path('data/processed/cleaned_collection.csv')
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    cleaned_df.to_csv(output_dir, index=False)

    return cleaned_df

cleanup(load_data())