import pandas as pd

def clean_data(file_path):
    """Cleans raw transaction data."""
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data["amount"] = data["amount"].apply(lambda x: abs(x))
    return data

def normalize_data(data):
    """Normalizes transaction amounts."""
    data["amount"] /= data["amount"].max()
    return data

if __name__ == "__main__":
    raw_data = clean_data("data/raw/transactions.csv")
    normalized_data = normalize_data(raw_data)
    normalized_data.to_csv("data/processed/transactions_normalized.csv", index=False)
