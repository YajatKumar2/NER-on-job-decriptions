import pandas as pd
import spacy

def load_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = load_data('dataset.csv')
    print(f"Data loaded: {df.shape}")
